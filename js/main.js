// Foloe 官网通用脚本
(function () {
    // 移动端导航
    var toggle = document.querySelector('.nav-toggle');
    var menu = document.querySelector('.nav-menu');
    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            menu.classList.toggle('open');
        });
    }
    // 移动端下拉
    document.querySelectorAll('.nav-menu > li.has-sub > a').forEach(function (link) {
        link.addEventListener('click', function (e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                var dd = link.parentElement.querySelector('.dropdown');
                if (dd) dd.classList.toggle('show');
            }
        });
    });
    // 点击菜单外区域时关闭移动端菜单
    document.addEventListener('click', function (e) {
        if (!menu || !menu.classList.contains('open')) return;
        var header = document.querySelector('.header');
        if (header && !header.contains(e.target)) {
            menu.classList.remove('open');
        }
    });
    // 窗口放大到桌面尺寸时复位移动端状态
    window.addEventListener('resize', function () {
        if (window.innerWidth > 768 && menu) {
            menu.classList.remove('open');
            menu.querySelectorAll('.dropdown.show').forEach(function (d) { d.classList.remove('show'); });
        }
    });
})();

// 数字滚动动画
(function () {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length) return;
    function run(el) {
        var target = parseInt(el.getAttribute('data-count'), 10) || 0;
        var dur = 1600;
        var start = null;
        function step(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.floor(eased * target);
            if (p < 1) requestAnimationFrame(step);
            else el.textContent = target;
        }
        requestAnimationFrame(step);
    }
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { run(en.target); io.unobserve(en.target); }
            });
        }, { threshold: 0.4 });
        els.forEach(function (el) { io.observe(el); });
    } else {
        els.forEach(run);
    }
})();

// 产品详情缩略图切换
(function () {
    var main = document.querySelector('.pd-gallery .main-pic img');
    var thumbs = document.querySelectorAll('.pd-gallery .thumbs img');
    if (!main || !thumbs.length) return;
    thumbs.forEach(function (t) {
        t.addEventListener('click', function () {
            main.src = t.getAttribute('data-full') || t.src;
            thumbs.forEach(function (x) { x.classList.remove('on'); });
            t.classList.add('on');
        });
    });
})();

// 产品详情页
(function () {
    var card = document.querySelector('.pd-wrap');
    if (!card) return;
    var title = card.parentElement ? card.parentElement.querySelector('.mc-title') : null;
    var target = title || card;
    var header = document.querySelector('.header');
    var offset = header ? header.offsetHeight : 76;
    var y = target.getBoundingClientRect().top + window.scrollY - offset - 16;
    window.scrollTo({ top: Math.max(0, y), left: 0, behavior: 'instant' });
})();

function switchImage(elem, className) {
    var mainImg = document.getElementById('mainImage');
    mainImg.src = elem.getAttribute('data-full');
    mainImg.className = className;
}
