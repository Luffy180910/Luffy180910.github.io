/**
 * Cyberpunk Navigation Bar Injector
 * Injects a fixed top nav into every page, highlights current section.
 */
(function() {
  'use strict';

  var sections = [
    { name: '首页',  path: '/pages/home/',     url: '/pages/home/index.html' },
    { name: '博客',  path: '/pages/blog/',     url: '/pages/blog/index.html' },
    { name: '视频',  path: '/pages/video/',    url: '/pages/video/index.html' },
    { name: '算法',  path: '/pages/algorithm/',url: '/pages/algorithm/index.html' },
    { name: '数学',  path: '/pages/mathematics/',url: '/pages/mathematics/index.html' },
    { name: '原神',  path: '/pages/genshin/',  url: '/pages/genshin/index.html' },
    { name: '德州',  path: '/pages/texas/',    url: '/pages/texas/index.html' },
    { name: 'WebGL', path: '/projects/webgl-coursework/', url: '/projects/webgl-coursework/WebGL.html' }
  ];

  var currentPath = window.location.pathname;
  var activeIndex = -1;

  // Find the best matching section
  sections.forEach(function(s, i) {
    if (currentPath.indexOf(s.path) !== -1) {
      // Prefer longer (more specific) path matches
      if (activeIndex === -1 || s.path.length > sections[activeIndex].path.length) {
        activeIndex = i;
      }
    }
  });

  // Handle root redirect pages
  if (currentPath === '/' || currentPath === '/index.html') {
    activeIndex = 0;
  }
  if (currentPath === '/texas.html') {
    activeIndex = 6;
  }

  // Build nav HTML
  var linksHtml = '';
  sections.forEach(function(s, i) {
    var cls = (i === activeIndex) ? ' class="active"' : '';
    linksHtml += '<a href="' + s.url + '"' + cls + '>' + s.name + '</a>';
  });

  var navHtml =
    '<a href="/pages/home/index.html" class="nav-brand">&diams; LUFFY</a>' +
    '<button class="nav-hamburger" id="nav-hamburger" aria-label="Menu">&#9776;</button>' +
    '<div class="nav-links">' + linksHtml + '</div>';

  // Create nav element
  var nav = document.createElement('nav');
  nav.id = 'cyber-nav';
  nav.innerHTML = navHtml;

  // Create mobile overlay
  var overlay = document.createElement('div');
  overlay.className = 'nav-overlay';
  overlay.id = 'nav-overlay';
  var overlayLinks = '';
  sections.forEach(function(s, i) {
    var cls = (i === activeIndex) ? ' class="active"' : '';
    overlayLinks += '<a href="' + s.url + '"' + cls + '>' + s.name + '</a>';
  });
  overlay.innerHTML = overlayLinks;

  // Insert into DOM
  if (document.body) {
    document.body.insertBefore(overlay, document.body.firstChild);
    document.body.insertBefore(nav, document.body.firstChild);
    document.body.classList.add('has-cyber-nav');
  } else {
    // DOM not ready yet, wait
    document.addEventListener('DOMContentLoaded', function() {
      document.body.insertBefore(overlay, document.body.firstChild);
      document.body.insertBefore(nav, document.body.firstChild);
      document.body.classList.add('has-cyber-nav');
    });
  }

  // Hamburger toggle
  function setupHamburger() {
    var btn = document.getElementById('nav-hamburger');
    var ov = document.getElementById('nav-overlay');
    if (!btn || !ov) return;

    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      ov.classList.toggle('open');
      btn.innerHTML = ov.classList.contains('open') ? '&#10005;' : '&#9776;';
    });

    // Close on link click
    ov.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        ov.classList.remove('open');
        btn.innerHTML = '&#9776;';
      });
    });

    // Close on outside click
    document.addEventListener('click', function(e) {
      if (!ov.classList.contains('open')) return;
      if (!ov.contains(e.target) && e.target !== btn) {
        ov.classList.remove('open');
        btn.innerHTML = '&#9776;';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupHamburger);
  } else {
    setupHamburger();
  }
})();
