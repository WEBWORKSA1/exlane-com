/* ExLane.com — site runtime (no dependencies)
   - theme toggle, mobile nav, reveal-on-scroll
   - contact routing: the site's single contact address is never written
     in the markup. It is assembled at click-time from encoded parts.
   - forms: every form on the site is delivered through the same hidden
     address (mailto with a pre-filled body). Swap CONFIG.endpoint for a
     Formspree/Basin/Netlify endpoint to get server-side delivery.
   - lightweight YouTube facade, newsletter capture, quick-exit.
*/
(function () {
  "use strict";

  var CONFIG = {
    endpoint: "",                     // optional: e.g. "https://formspree.io/f/xxxxxxx"
    // Encoded contact route. Do not replace with a plain address anywhere in HTML.
    k: "d2Vid29ya3NhMUBnbWFpbC5jb20=",
    siteName: "ExLane"
  };

  function route() { try { return atob(CONFIG.k); } catch (e) { return ""; } }

  /* ---------- theme ---------- */
  var root = document.documentElement;
  function applyTheme(t) { root.setAttribute("data-theme", t); try { localStorage.setItem("exlane-theme", t); } catch (e) {}
    document.querySelectorAll("[data-theme-toggle]").forEach(function (b) { b.setAttribute("aria-label", t === "dark" ? "Switch to light mode" : "Switch to dark mode"); b.textContent = t === "dark" ? "☀" : "☾"; }); }
  (function initTheme() {
    var saved = null; try { saved = localStorage.getItem("exlane-theme"); } catch (e) {}
    var pref = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    applyTheme(saved || pref);
  })();
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]"); if (!t) return;
    applyTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  /* ---------- mobile nav ---------- */
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-nav-toggle]");
    var menu = document.getElementById("menu");
    if (b && menu) { var open = menu.classList.toggle("open"); b.setAttribute("aria-expanded", open ? "true" : "false"); return; }
    if (menu && !e.target.closest("#menu") && !e.target.closest("[data-nav-toggle]")) menu.classList.remove("open");
  });

  /* ---------- current page highlight ---------- */
  (function () {
    var here = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll("#menu a").forEach(function (a) {
      var href = a.getAttribute("href").split("/").pop();
      if (href === here) a.setAttribute("aria-current", "page");
    });
  })();

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    root.classList.add("js");
    setTimeout(function () { document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); }); }, 1500);
    var io = new IntersectionObserver(function (entries) { entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: .12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else { document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  /* ---------- contact links (hidden address) ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-contact]"); if (!a) return;
    e.preventDefault();
    var subject = a.getAttribute("data-subject") || (CONFIG.siteName + " inquiry");
    window.location.href = "mailto:" + route() + "?subject=" + encodeURIComponent(subject);
  });

  /* ---------- forms ---------- */
  function serialize(form) {
    var out = [], fd = new FormData(form);
    fd.forEach(function (v, k) { if (k === "_gotcha") return; out.push(k.replace(/_/g, " ") + ": " + v); });
    return out.join("\n");
  }
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("form[data-form]"); if (!form) return;
    e.preventDefault();
    if (form.querySelector("[name=_gotcha]") && form.querySelector("[name=_gotcha]").value) return; // honeypot
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var kind = form.getAttribute("data-form") || "Form";
    var subject = "[" + CONFIG.siteName + "] " + kind;
    var body = serialize(form) + "\n\nSent from: " + location.href;
    var done = function () {
      var ok = form.querySelector(".form-success") || form.parentElement.querySelector(".form-success");
      if (ok) { ok.classList.add("show"); ok.scrollIntoView({ behavior: "smooth", block: "nearest" }); }
      form.reset();
      try { localStorage.setItem("exlane-lead-" + kind, "1"); } catch (err) {}
    };
    if (CONFIG.endpoint) {
      var fd = new FormData(form); fd.append("_subject", subject);
      fetch(CONFIG.endpoint, { method: "POST", body: fd, headers: { Accept: "application/json" } }).then(done).catch(function () { window.location.href = "mailto:" + route() + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body); done(); });
    } else {
      window.location.href = "mailto:" + route() + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      done();
    }
  });

  /* ---------- chips (multi-select tags inside forms) ---------- */
  document.addEventListener("click", function (e) {
    var c = e.target.closest(".chips .chip"); if (!c) return;
    var group = c.parentElement, single = group.hasAttribute("data-single");
    if (single) group.querySelectorAll(".chip").forEach(function (x) { x.classList.remove("active"); });
    c.classList.toggle("active");
    var hidden = group.parentElement.querySelector("input[type=hidden][data-chips]");
    if (hidden) hidden.value = Array.prototype.map.call(group.querySelectorAll(".chip.active"), function (x) { return x.textContent.trim(); }).join(", ");
  });

  /* ---------- YouTube facade ---------- */
  document.addEventListener("click", function (e) {
    var f = e.target.closest(".video-facade"); if (!f) return;
    var src = f.getAttribute("data-src"); var wrap = f.parentElement;
    var ifr = document.createElement("iframe");
    ifr.src = src + (src.indexOf("?") > -1 ? "&" : "?") + "autoplay=1";
    ifr.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    ifr.allowFullscreen = true; ifr.title = f.getAttribute("data-title") || "Video";
    wrap.appendChild(ifr); f.remove();
  });

  /* ---------- quick exit (safety pattern) ---------- */
  function quickExit() { try { window.open("https://www.google.com", "_newtab"); } catch (e) {} window.location.replace("https://www.google.com"); }
  document.addEventListener("click", function (e) { if (e.target.closest("[data-quick-exit]")) quickExit(); });
  var escCount = 0, escTimer;
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { escCount++; clearTimeout(escTimer); escTimer = setTimeout(function () { escCount = 0; }, 800); if (escCount >= 2) quickExit(); } });

  /* ---------- share buttons ---------- */
  document.addEventListener("click", function (e) {
    var s = e.target.closest("[data-share]"); if (!s) return;
    e.preventDefault();
    var url = location.href, title = document.title, net = s.getAttribute("data-share");
    var map = {
      x: "https://twitter.com/intent/tweet?url=" + encodeURIComponent(url) + "&text=" + encodeURIComponent(title),
      fb: "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(url),
      wa: "https://wa.me/?text=" + encodeURIComponent(title + " " + url),
      li: "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(url)
    };
    if (net === "copy") { navigator.clipboard && navigator.clipboard.writeText(url); s.textContent = "Copied!"; return; }
    if (net === "native" && navigator.share) { navigator.share({ title: title, url: url }); return; }
    if (map[net]) window.open(map[net], "_blank", "noopener,width=600,height=500");
  });

  /* ---------- footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- exit-intent newsletter (desktop, once per 7 days) ---------- */
  (function () {
    var modal = document.getElementById("exit-modal"); if (!modal) return;
    var key = "exlane-exit-seen", seen = null; try { seen = localStorage.getItem(key); } catch (e) {}
    if (seen && Date.now() - Number(seen) < 7 * 864e5) return;
    var shown = false;
    document.addEventListener("mouseout", function (e) {
      if (shown || e.clientY > 8 || e.relatedTarget) return;
      shown = true; modal.hidden = false; try { localStorage.setItem(key, String(Date.now())); } catch (err) {}
    });
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest("[data-close]")) modal.hidden = true; });
  })();

  window.ExLane = { route: route, config: CONFIG };
})();
