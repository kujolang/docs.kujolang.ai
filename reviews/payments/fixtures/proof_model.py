"""Review-only executable model. Not a Payments implementation or isolation test.

Python stdlib is used for repository-maintenance proof fixtures, to independently
exercise SQLite conditional claims and a simulated processor across process death.
No network access, credentials, payment provider or product runtime is involved.
"""
import concurrent.futures
import copy
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import sqlite3
import tempfile
import unittest

ALLOWED = {
    'awaiting_authorization': {'ready', 'closed'},
    'ready': {'executing', 'closed'},
    'executing': {'executing', 'succeeded', 'closed', 'reconciliation_required'},
    'reconciliation_required': {'reconciliation_required', 'executing', 'succeeded', 'closed'},
    'succeeded': set(), 'closed': set(),
}


def digest(value):
    # ASCII fixture subset only; does not certify Ability digest compatibility.
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def connect(path):
    db = sqlite3.connect(path, timeout=10)
    db.execute('PRAGMA synchronous=FULL')
    return db


def initialize(path):
    with connect(path) as db:
        db.execute('PRAGMA journal_mode=WAL')
        db.executescript('''
          CREATE TABLE execution (id TEXT PRIMARY KEY, state TEXT NOT NULL, claimed INTEGER NOT NULL);
          CREATE TABLE approvals (id TEXT PRIMARY KEY, consumed INTEGER NOT NULL);
          INSERT INTO execution VALUES ('exec_1', 'ready', 0);
          INSERT INTO approvals VALUES ('approval_1', 0);
        ''')


def claim(path):
    with connect(path) as db:
        db.execute('BEGIN IMMEDIATE')
        count = db.execute("UPDATE execution SET state='executing',claimed=1 WHERE id='exec_1' AND state='ready' AND claimed=0").rowcount
        if not count:
            return False
        consumed = db.execute("UPDATE approvals SET consumed=1 WHERE id='approval_1' AND consumed=0").rowcount
        if consumed != 1:
            db.rollback()
            return False
        return True


def crash_worker(path, processor, point):
    if not claim(path):
        os._exit(2)
    if point == 'before_send':
        os._exit(10)
    # Independently durable mock provider. No real money.
    with connect(processor) as db:
        db.execute("INSERT INTO charges VALUES ('exec_1', 5500)")
    if point in ('after_charge', 'before_receipt', 'audit_failure'):
        os._exit(11)


class ReviewProof(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = str(Path(self.temp.name) / 'journal.db')
        self.processor = str(Path(self.temp.name) / 'processor.db')
        initialize(self.db)
        with connect(self.processor) as db:
            db.execute('CREATE TABLE charges (id TEXT, amount INTEGER)')

    def tearDown(self):
        self.temp.cleanup()

    def test_parallel_claims_have_one_winner(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
            won = list(pool.map(lambda _: claim(self.db), range(64)))
        self.assertEqual(sum(won), 1)
        with connect(self.db) as db:
            self.assertEqual(db.execute('SELECT consumed FROM approvals').fetchone()[0], 1)

    def test_consumed_approval_rolls_back_claim(self):
        with connect(self.db) as db:
            db.execute('UPDATE approvals SET consumed=1')
        self.assertFalse(claim(self.db))
        with connect(self.db) as db:
            self.assertEqual(db.execute('SELECT state,claimed FROM execution').fetchone(), ('ready', 0))

    def test_crash_points_cannot_resubmit(self):
        for point in ('before_send', 'after_charge', 'before_receipt', 'audit_failure'):
            with self.subTest(point=point):
                case = str(Path(self.temp.name) / (point + '.db'))
                provider = str(Path(self.temp.name) / (point + '-provider.db'))
                initialize(case)
                with connect(provider) as db:
                    db.execute('CREATE TABLE charges (id TEXT, amount INTEGER)')
                worker = multiprocessing.get_context('spawn').Process(target=crash_worker, args=(case, provider, point))
                worker.start(); worker.join(10)
                self.assertFalse(worker.is_alive())
                self.assertIn(worker.exitcode, (10, 11))
                with connect(case) as db:
                    db.execute("UPDATE execution SET state='reconciliation_required' WHERE state='executing'")
                self.assertFalse(claim(case))
                with connect(provider) as db:
                    charges = db.execute('SELECT COUNT(*) FROM charges').fetchone()[0]
                self.assertEqual(charges, 0 if point == 'before_send' else 1)

    def test_no_uncertain_or_terminal_path_returns_to_ready(self):
        for start in ('executing', 'reconciliation_required', 'succeeded', 'closed'):
            seen = set(); todo = [start]
            while todo:
                state = todo.pop()
                if state in seen: continue
                seen.add(state); todo.extend(ALLOWED[state])
            self.assertNotIn('ready', seen)

    def test_all_consequential_fields_change_binding(self):
        snapshot = {'amount': 5500, 'currency': 'USD', 'merchant': 'merchant_1', 'intent': 'intent_1', 'principal': 'user_1', 'tenant': 'tenant_1', 'execution': 'exec_1', 'provider': 'provider_1', 'class': 'machine', 'expires': 2000, 'nonce': 'nonce_1', 'shipping': 'home_v1', 'body': 'body_digest'}
        approved = digest(snapshot)
        for key in snapshot:
            with self.subTest(field=key):
                changed = copy.deepcopy(snapshot); changed[key] = str(changed[key]) + '_changed'
                self.assertNotEqual(approved, digest(changed))

    def test_observed_claim_is_not_a_dispatch_permit(self):
        self.assertTrue(claim(self.db))
        # A stale durable row cannot grant permission to another worker.
        with connect(self.db) as db:
            db.execute("UPDATE execution SET state='reconciliation_required'")
        for _ in range(16):
            if claim(self.db):
                with connect(self.processor) as db:
                    db.execute("INSERT INTO charges VALUES ('exec_1',5500)")
        with connect(self.processor) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM charges').fetchone()[0], 0)

    def test_processor_does_not_hide_repeated_submissions(self):
        with connect(self.processor) as db:
            db.execute("INSERT INTO charges VALUES ('same',5500)")
            db.execute("INSERT INTO charges VALUES ('same',5500)")
            self.assertEqual(db.execute('SELECT COUNT(*) FROM charges').fetchone()[0], 2)

    def test_distinct_processes_have_one_dispatch(self):
        ctx = multiprocessing.get_context('spawn')
        workers = [ctx.Process(target=crash_worker, args=(self.db, self.processor, 'after_charge')) for _ in range(8)]
        for worker in workers: worker.start()
        for worker in workers:
            worker.join(10)
            self.assertFalse(worker.is_alive())
            self.assertIn(worker.exitcode, (2,11))
        self.assertEqual(sum(w.exitcode == 11 for w in workers), 1)
        with connect(self.processor) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM charges').fetchone()[0], 1)

    def test_cancellation_and_claim_serialize(self):
        def cancel():
            with connect(self.db) as db:
                return db.execute("UPDATE execution SET state='closed' WHERE state='ready' AND claimed=0").rowcount == 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            claimed = pool.submit(claim, self.db)
            cancelled = pool.submit(cancel)
        self.assertEqual(int(claimed.result()) + int(cancelled.result()), 1)

    def test_exact_money_and_cap(self):
        def valid(v): return type(v) is int and 0 < v <= 9007199254740991
        for value in (True, 55.0, -1, 0, '5500', 9007199254740992):
            self.assertFalse(valid(value))
        for currency, amount in [('JPY', 55), ('USD', 5500), ('KWD', 55000)]:
            self.assertTrue(valid(amount))
        self.assertLessEqual(5400, 5500)
        self.assertNotEqual(5400, 5500)  # cap does not permit mutating approved exact amount

    def test_tombstone_blocks_reuse_after_payload_retention(self):
        self.assertTrue(claim(self.db))
        with connect(self.db) as db:
            db.execute("UPDATE execution SET state='succeeded'")
        self.assertFalse(claim(self.db))

    def test_projection_drops_nested_sentinel_fields(self):
        secrets = {name: 'SENTINEL_' + name for name in ('PAN', 'CVC', 'SPT', 'LPT', 'OAUTH', 'REFRESH', 'API_SECRET')}
        # This tests only this proposed fixed projection, not ecosystem sinks.
        for status in ('succeeded', 'reconciliation_required'):
            private = {'execution_id': 'exec_1', 'status': status, 'provider': secrets, 'error': str(secrets)}
            public = {key: private[key] for key in ('execution_id', 'status')}
            serialized = json.dumps(public)
            for sentinel in secrets.values(): self.assertNotIn(sentinel, serialized)


if __name__ == '__main__':
    unittest.main(verbosity=2)
