(function() {
	var themeButton = document.querySelector('[data-docs-theme]');
	var root = document.documentElement;
	var themeColor = document.querySelector('meta[name="theme-color"]');
	var updateThemeControl = function() {
		var isDark = root.dataset.theme === 'kujo-dark';
		if (themeButton) {
			themeButton.setAttribute('aria-pressed', isDark ? 'true' : 'false');
			themeButton.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
			themeButton.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
		}
		if (themeColor) {
			themeColor.setAttribute('content', isDark ? '#0b0b0b' : '#ffffff');
		}
	};
	updateThemeControl();
	if (themeButton) {
		themeButton.addEventListener('click', function() {
			root.dataset.theme = root.dataset.theme === 'kujo-dark' ? 'kujo-light' : 'kujo-dark';
			try { window.localStorage.setItem('sk-theme', root.dataset.theme); } catch (error) {}
			updateThemeControl();
		});
	}

	var menuButton = document.querySelector('[data-docs-menu]');
	var primaryNavigation = document.getElementById('primary-navigation');
	var topbar = document.querySelector('.docs-topbar');
	if (menuButton && primaryNavigation && topbar) {
		var setMenuOpen = function(isOpen, restoreFocus) {
			primaryNavigation.classList.toggle('is-open', isOpen);
			topbar.classList.toggle('is-menu-open', isOpen);
			document.documentElement.classList.toggle('docs-menu-open', isOpen);
			menuButton.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
			menuButton.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
			if (isOpen) {
				window.requestAnimationFrame(function() {
					var firstLink = primaryNavigation.querySelector('a');
					if (firstLink) {
						firstLink.focus();
					}
				});
			} else if (restoreFocus) {
				menuButton.focus();
			}
		};

		menuButton.addEventListener('click', function() {
			setMenuOpen(menuButton.getAttribute('aria-expanded') !== 'true', false);
		});

		primaryNavigation.querySelectorAll('a').forEach(function(link) {
			link.addEventListener('click', function() {
				setMenuOpen(false, false);
			});
		});

		document.addEventListener('keydown', function(event) {
			if (menuButton.getAttribute('aria-expanded') !== 'true') {
				return;
			}
			if (event.key === 'Escape') {
				event.preventDefault();
				setMenuOpen(false, true);
				return;
			}
			if (event.key !== 'Tab') {
				return;
			}
			var focusable = Array.prototype.slice.call(topbar.querySelectorAll('a, button, input'))
				.filter(function(element) { return !element.disabled && element.offsetParent !== null; });
			if (!focusable.length) {
				return;
			}
			var first = focusable[0];
			var last = focusable[focusable.length - 1];
			if (event.shiftKey && document.activeElement === first) {
				event.preventDefault();
				last.focus();
			} else if (!event.shiftKey && document.activeElement === last) {
				event.preventDefault();
				first.focus();
			}
		});

		var desktopNavigation = window.matchMedia('(min-width: 52.01rem)');
		var resetDesktopNavigation = function(event) {
			if (event.matches) {
				setMenuOpen(false, false);
			}
		};
		if (desktopNavigation.addEventListener) {
			desktopNavigation.addEventListener('change', resetDesktopNavigation);
		} else {
			desktopNavigation.addListener(resetDesktopNavigation);
		}
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
		return index.map(function(item, position) {
			var title = (item.title || '').toLowerCase();
			var description = (item.description || '').toLowerCase();
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
			if (haystack.indexOf(q) < 0) {
				return null;
			}
			var score = 4;
			if (title === q) {
				score = 0;
			} else if (title.indexOf(q) === 0) {
				score = 1;
			} else if (title.indexOf(q) >= 0) {
				score = 2;
			} else if (description.indexOf(q) >= 0) {
				score = 3;
			}
			return {item: item, score: score, position: position};
		}).filter(function(result) {
			return result !== null;
		}).sort(function(left, right) {
			return left.score - right.score || left.position - right.position;
		}).map(function(result) {
			return result.item;
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

	var syntaxRules = {
		bash: [
			['syntax-string', /"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/y],
			['syntax-comment', /#[^\n]*/y],
			['syntax-variable', /\$(?:\{[^}\n]+\}|[A-Za-z_][A-Za-z0-9_]*|\d+)/y],
			['syntax-flag', /--?[A-Za-z][A-Za-z0-9-]*/y],
			['syntax-command', /(?<![A-Za-z0-9_.-])(?:bash|cargo|cat|cd|command|cp|curl|git|kujo|mkdir|mv|npm|npx|python3?|rg|rm|sort)\b/y],
			['syntax-number', /\b\d+(?:\.\d+)?\b/y],
			['syntax-operator', /&&|\|\||[|\\;]/y]
		],
		kujo: [
			['syntax-string', /"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/y],
			['syntax-comment', /\/\/[^\n]*/y],
			['syntax-keyword', /\b(?:as|async|await|break|catch|continue|else|false|for|from|func|if|import|in|let|match|module|mut|null|pub|return|throw|true|try|while)\b/y],
			['syntax-command', /(?<![A-Za-z0-9_.-])kujo\b/y],
			['syntax-function', /\b[A-Za-z_][A-Za-z0-9_]*(?=\s*\()/y],
			['syntax-number', /\b\d+(?:\.\d+)?\b/y],
			['syntax-operator', /:=|==|!=|<=|>=|=>|[-+*/%=<>]/y]
		]
	};

	var appendSyntaxToken = function(fragment, className, value) {
		if (!className) {
			fragment.appendChild(document.createTextNode(value));
			return;
		}
		var token = document.createElement('span');
		token.className = className;
		token.textContent = value;
		fragment.appendChild(token);
	};

	var highlightCode = function(block) {
		var languageMatch = block.className.match(/(?:^|\s)language-([\w-]+)/);
		var language = languageMatch ? languageMatch[1].toLowerCase() : '';
		var rules = syntaxRules[language];
		if (!rules) {
			return;
		}
		var source = block.textContent;
		var fragment = document.createDocumentFragment();
		var plain = '';
		var index = 0;
		while (index < source.length) {
			var matchedClass = '';
			var matchedValue = '';
			for (var ruleIndex = 0; ruleIndex < rules.length; ruleIndex += 1) {
				var expression = rules[ruleIndex][1];
				expression.lastIndex = index;
				var match = expression.exec(source);
				if (match) {
					matchedClass = rules[ruleIndex][0];
					matchedValue = match[0];
					break;
				}
			}
			if (matchedValue) {
				if (plain) {
					appendSyntaxToken(fragment, '', plain);
					plain = '';
				}
				appendSyntaxToken(fragment, matchedClass, matchedValue);
				index += matchedValue.length;
			} else {
				plain += source.charAt(index);
				index += 1;
			}
		}
		if (plain) {
			appendSyntaxToken(fragment, '', plain);
		}
		block.replaceChildren(fragment);
		block.parentElement.classList.add('has-syntax-highlighting');
		block.parentElement.dataset.languageLabel = language === 'bash' ? 'Terminal' : 'Kujo';
	};

	document.querySelectorAll('pre > code[class*="language-"]').forEach(highlightCode);

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

	var renderCopyButton = function(button, state) {
		var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
		svg.setAttribute('viewBox', '0 0 24 24');
		svg.setAttribute('aria-hidden', 'true');
		var paths = state === 'copied'
			? ['M5 12l5 5L20 7']
			: ['M7 8m0 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2z', 'M13 8V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h3'];
		paths.forEach(function(pathData) {
			var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
			path.setAttribute('d', pathData);
			svg.appendChild(path);
		});
		var label = state === 'copied' ? 'Copied' : state === 'manual' ? 'Code selected; copy manually' : 'Copy code';
		button.replaceChildren(svg);
		button.dataset.copyState = state;
		button.setAttribute('aria-label', label);
		button.title = label;
	};

	var bindCopyButton = function(button, block) {
		renderCopyButton(button, 'copy');
		button.addEventListener('click', function() {
			copyText(block.textContent).then(function() {
				renderCopyButton(button, 'copied');
				window.setTimeout(function() { renderCopyButton(button, 'copy'); }, 3000);
			}).catch(function() {
				var selection = window.getSelection();
				var range = document.createRange();
				range.selectNodeContents(block);
				selection.removeAllRanges();
				selection.addRange(range);
				renderCopyButton(button, 'manual');
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
		button.setAttribute('data-copy-code', '');
		bindCopyButton(button, block.querySelector('code') || block);
		var shell = document.createElement('div');
		shell.className = 'docs-code-shell';
		block.parentNode.insertBefore(shell, block);
		shell.appendChild(block);
		shell.appendChild(button);
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
