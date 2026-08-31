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

// 新闻标签切换（首页 / 列表页）
(function () {
    var tabs = document.querySelectorAll('.news-tabs button');
    var items = document.querySelectorAll('.news-list .nl-item[data-cat]');
    if (!tabs.length) return;
    tabs.forEach(function (btn, idx) {
        btn.addEventListener('click', function () {
            tabs.forEach(function (b) { b.classList.remove('on'); });
            btn.classList.add('on');
            var cat = btn.getAttribute('data-cat') || '';
            items.forEach(function (it) {
                it.style.display = (!cat || it.getAttribute('data-cat') === cat) ? '' : 'none';
            });
        });
    });
})();

// 侧边栏锚点高亮
(function () {
    var links = document.querySelectorAll('.side ul li a[href*="#"]');
    if (!links.length) return;
    function setActive(id) {
        links.forEach(function (a) {
            a.classList.toggle('on', a.getAttribute('href').indexOf(id) !== -1);
        });
    }
    var first = document.querySelector('main [id], .main-col [id]');
    if (first) setActive(first.id);
})();
