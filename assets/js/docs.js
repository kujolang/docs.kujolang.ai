(function() {
	var menuButton = document.querySelector('[data-docs-menu]');
	var primaryNavigation = document.getElementById('primary-navigation');
	if (menuButton && primaryNavigation) {
		menuButton.addEventListener('click', function() {
			var isOpen = primaryNavigation.classList.toggle('is-open');
			menuButton.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
		});
	}

	document.querySelectorAll('.docs-sidebar a').forEach(function(link) {
		var currentPath = window.location.pathname.replace(/index\.html$/, '');
		var linkPath = new URL(link.href, window.location.origin).pathname.replace(/index\.html$/, '');
		if (currentPath === linkPath || (linkPath !== '/' && currentPath.indexOf(linkPath) === 0)) {
			link.setAttribute('aria-current', 'page');
		}
	});

	var input = document.getElementById('docs-search');
	var panel = document.getElementById('docs-search-results');
	var index = [];

	var render = function(items, query) {
		if (!panel) {
			return;
		}
		if (!query) {
			panel.classList.remove('is-open');
			panel.innerHTML = '';
			return;
		}
		if (!items.length) {
			panel.innerHTML = '<p class="docs-search-empty">No results found.</p>';
			panel.classList.add('is-open');
			return;
		}
		panel.innerHTML = items.slice(0, 8).map(function(item) {
			var description = item.description || item.section || item.route || '';
			return '<a href="' + item.url + '"><strong>' + item.title + '</strong><span>' + description + '</span></a>';
		}).join('');
		panel.classList.add('is-open');
	};

	var search = function(query) {
		var q = query.trim().toLowerCase();
		if (!q) {
			return [];
		}
		return index.filter(function(item) {
			var haystack = [
				item.title,
				item.description,
				item.section,
				item.audience,
				item.difficulty,
				item.status,
				item.version,
				(item.tags || []).join(' '),
				(item.headings || []).join(' '),
				item.text
			].join(' ').toLowerCase();
			return haystack.indexOf(q) >= 0;
		});
	};

	if (input && panel) {
		fetch('/assets/js/docs-search-index.json')
			.then(function(response) { return response.ok ? response.json() : {items: []}; })
			.then(function(payload) { index = payload.items || []; })
			.catch(function() { index = []; });

		input.addEventListener('input', function() {
			render(search(input.value), input.value.trim());
		});
		input.addEventListener('keydown', function(event) {
			if (event.key === 'Escape') {
				input.value = '';
				render([], '');
			}
		});
		document.addEventListener('click', function(event) {
			if (!panel.contains(event.target) && event.target !== input) {
				panel.classList.remove('is-open');
			}
		});
	}

	var legacyCopyText = function(text) {
		return new Promise(function(resolve, reject) {
			var textarea = document.createElement('textarea');
			textarea.value = text;
			textarea.setAttribute('readonly', '');
			textarea.style.position = 'fixed';
			textarea.style.opacity = '0';
			document.body.appendChild(textarea);
			textarea.select();
			try {
				if (!document.execCommand('copy')) {
					throw new Error('Copy command was rejected');
				}
				resolve();
			} catch (error) {
				reject(error);
			} finally {
				document.body.removeChild(textarea);
			}
		});
	};

	var copyText = function(text) {
		return legacyCopyText(text).catch(function() {
			if (navigator.clipboard && window.isSecureContext) {
				return navigator.clipboard.writeText(text);
			}
			return Promise.reject(new Error('Clipboard access is unavailable'));
		});
	};

	var bindCopyButton = function(button, block) {
		button.addEventListener('click', function() {
			copyText(block.textContent).then(function() {
				button.textContent = 'Copied';
				window.setTimeout(function() { button.textContent = 'Copy'; }, 3000);
			}).catch(function() {
				var selection = window.getSelection();
				var range = document.createRange();
				range.selectNodeContents(block);
				selection.removeAllRanges();
				selection.addRange(range);
				button.textContent = 'Select and copy';
			});
		});
	};

	document.querySelectorAll('[data-copy-code]').forEach(function(button) {
		var container = button.closest('.sk-code-block') || button.parentElement;
		var block = container ? container.querySelector('pre code, pre') : null;
		if (block) {
			bindCopyButton(button, block);
		}
	});

	document.querySelectorAll('pre').forEach(function(block) {
		if (block.closest('.sk-code-block') && block.closest('.sk-code-block').querySelector('[data-copy-code]')) {
			return;
		}
		var button = document.createElement('button');
		button.type = 'button';
		button.className = 'copy-code-button';
		button.textContent = 'Copy';
		bindCopyButton(button, block);
		block.appendChild(button);
	});

	document.querySelectorAll('.docs-body h2, .docs-body h3').forEach(function(heading) {
		if (heading.id) {
			return;
		}
		var slug = heading.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section';
		var candidate = slug;
		var count = 2;
		while (document.getElementById(candidate)) {
			candidate = slug + '-' + count;
			count += 1;
		}
		heading.id = candidate;
	});
})();
