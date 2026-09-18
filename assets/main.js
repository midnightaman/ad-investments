// AD Investments — shared behaviour for index + all service pages

// Custom cursor
(function () {
  var cursor = document.getElementById('cursor');
  var follower = document.getElementById('follower');
  if (!cursor || !follower) return;
  var fx = 0, fy = 0, cx = 0, cy = 0;

  document.addEventListener('mousemove', function (e) {
    cx = e.clientX; cy = e.clientY;
    cursor.style.left = cx + 'px';
    cursor.style.top = cy + 'px';
  });

  function animateFollower() {
    fx += (cx - fx) * 0.12;
    fy += (cy - fy) * 0.12;
    follower.style.left = fx + 'px';
    follower.style.top = fy + 'px';
    requestAnimationFrame(animateFollower);
  }
  animateFollower();
})();

// Scroll reveal
(function () {
  var reveals = document.querySelectorAll('.reveal');

  function checkReveals() {
    reveals.forEach(function (el) {
      var rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 50) {
        el.classList.add('visible');
      }
    });
  }

  window.addEventListener('scroll', checkReveals);
  window.addEventListener('load', checkReveals);
  document.addEventListener('DOMContentLoaded', checkReveals);
  setTimeout(checkReveals, 100);
  setTimeout(checkReveals, 500);
})();

// Mobile nav menu
(function () {
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('mobileMenu');
  if (!toggle || !menu) return;

  function closeMenu() {
    menu.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', function () {
    var isOpen = menu.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  menu.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', closeMenu);
  });

  var svcToggle = menu.querySelector('.mobile-menu-services-toggle');
  var svcPanel = menu.querySelector('.mobile-menu-services');
  if (svcToggle && svcPanel) {
    svcToggle.addEventListener('click', function () {
      svcToggle.classList.toggle('open');
      svcPanel.classList.toggle('open');
    });
  }

  window.addEventListener('resize', function () {
    if (window.innerWidth > 768) closeMenu();
  });
})();

// Contact form -> WhatsApp
function sendToWhatsApp(e) {
  e.preventDefault();
  var name = document.getElementById('fname').value;
  var phone = document.getElementById('fphone').value;
  var interestEl = document.getElementById('finterest');
  var interest = interestEl ? interestEl.value : '';
  var message = document.getElementById('fmessage').value || 'No message';
  var text = 'Hello AD Investments! %F0%9F%91%8B%0A%0A*New Consultation Request*%0A%0A*Name:* ' + name + '%0A*Phone:* ' + phone + '%0A*Interested In:* ' + interest + '%0A*Message:* ' + message;
  window.open('https://wa.me/917379008786?text=' + text, '_blank');
}
