#!/usr/bin/env python3
"""ExLane.com static site generator.

Usage:  python3 tools/build.py
Reads page definitions from tools/pages.py and tools/articles.py and writes
finished HTML into the repository root (GitHub Pages serves it as-is).
No dependencies beyond the Python standard library.
"""
import os, sys, datetime, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages, articles  # noqa: E402

SITE = "https://exlane.com"
SITE_NAME = "ExLane"
TAGLINE = "The fast lane past your ex"
NOTICE_TEXT = "contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership"
NOTICE_LINK = "https://web.works/contact"
ADSENSE_CLIENT = "ca-pub-0000000000000000"   # replace with the real publisher id
GA_ID = ""                                   # e.g. "G-XXXXXXXXXX" (optional)

NAV = [
    ("Start Here", "start-here.html"),
    ("Quiz", "quiz.html"),
    ("Tools", "tools.html"),
    ("Guides", "articles.html"),
    ("Videos", "videos.html"),
    ("Stories", "stories.html"),
    ("Coaching", "coaching.html"),
    ("Support Us", "donate.html"),
]

LOGO_SVG = """<svg class="mark" viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8563f"/><stop offset="1" stop-color="#6d4be6"/></linearGradient></defs><rect width="40" height="40" rx="10" fill="url(#g)"/><path d="M8 30 L20 8 L32 30" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 8 L20 30" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="1 5"/></svg>"""


def head(p, depth):
    base = "../" * depth
    title = p.get("title", SITE_NAME)
    full = f"{title} | {SITE_NAME}" if p.get("path") != "index.html" else f"{SITE_NAME} — {TAGLINE}: Breakup Recovery, No-Contact Tools & Coaching"
    desc = html.escape(p.get("desc", ""))
    canonical = f"{SITE}/{p['path']}" if p["path"] != "index.html" else SITE + "/"
    ga = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>""" if GA_ID else ""
    jsonld = p.get("jsonld", "")
    base404 = ("<script>(function(){var h=location.hostname,p=location.pathname;var b=/github\\.io$/.test(h)?'/'+p.split('/')[1]+'/':'/';"
               "document.write('<base href=\"'+location.origin+b+'\">');})();</script>") if p["path"] == "404.html" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#e8563f">
{base404}
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{base}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
<script>try{{var t=localStorage.getItem('exlane-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<!-- Google AdSense: replace the client id in tools/build.py and rebuild, then add the same id to ads.txt -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>
{ga}
{jsonld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="notice-bar"><a href="{NOTICE_LINK}" rel="noopener" target="_blank">{NOTICE_TEXT}</a></div>
<header class="header"><div class="wrap nav">
  <a class="logo" href="{base}index.html" aria-label="ExLane home">{LOGO_SVG}<span>Ex<em>Lane</em></span></a>
  <ul class="menu" id="menu">{''.join(f'<li><a href="{base}{h}">{n}</a></li>' for n, h in NAV)}</ul>
  <div class="nav-actions">
    <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">☾</button>
    <a class="btn btn-primary btn-sm" href="{base}coaching.html">Get Matched</a>
    <button class="icon-btn burger" data-nav-toggle aria-controls="menu" aria-expanded="false" aria-label="Open menu">☰</button>
  </div>
</div></header>
<main id="main">
"""


def footer(depth):
    base = "../" * depth
    return f"""
</main>
<footer class="footer"><div class="wrap">
  <div class="footer-grid">
    <div>
      <a class="logo" href="{base}index.html">{LOGO_SVG}<span>Ex<em>Lane</em></span></a>
      <p class="muted" style="margin-top:12px">{TAGLINE}. Evidence-informed breakup recovery: no-contact tools, guides, videos, a community of people who got through it, and coaches when you need one.</p>
      <div class="crisis"><b>In crisis?</b> If you're thinking about harming yourself, contact your local emergency number or a crisis line now (US &amp; Canada: call or text <b>988</b>; UK &amp; ROI: Samaritans <b>116 123</b>; India: iCall <b>9152987821</b>). ExLane is not a substitute for professional care.</div>
    </div>
    <div><h4>Recover</h4><ul>
      <li><a href="{base}start-here.html">Start here</a></li><li><a href="{base}quiz.html">Are you over your ex? Quiz</a></li><li><a href="{base}tools.html">No-contact tracker &amp; tools</a></li><li><a href="{base}articles.html">Guides</a></li><li><a href="{base}videos.html">Videos</a></li></ul></div>
    <div><h4>Community</h4><ul>
      <li><a href="{base}stories.html">Recovery stories</a></li><li><a href="{base}stories.html#submit">Share your story</a></li><li><a href="{base}contests.html">Contests &amp; prizes</a></li><li><a href="{base}coaching.html">Find a coach</a></li></ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="{base}about.html">About</a></li><li><a href="{base}donate.html">Support ExLane</a></li><li><a href="{base}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{base}advertise.html#partners">Partnerships</a></li><li><a href="{base}careers.html">Careers &amp; talent</a></li><li><a href="{base}contact.html">Contact</a></li></ul></div>
    <div><h4>Legal</h4><ul>
      <li><a href="{base}privacy.html">Privacy policy</a></li><li><a href="{base}terms.html">Terms of use</a></li><li><a href="{base}disclaimer.html">Disclaimers &amp; trademark notice</a></li><li><a href="{base}sitemap.xml">Sitemap</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <span>© <span data-year>2026</span> ExLane.com. All rights reserved. Not medical, legal, or therapeutic advice.</span>
    <span>ExLane is an independent publication and is not affiliated with any similarly named company or mark. <a href="{base}disclaimer.html">Trademark notice</a>.</span>
  </div>
</div></footer>
<div class="sticky-cta"><a class="btn btn-grad" href="{base}quiz.html">Take the 2-minute quiz →</a></div>
<button class="quick-exit" data-quick-exit title="Leave this site instantly (or press Esc twice)">Quick exit ✕</button>
<div id="exit-modal" hidden style="position:fixed;inset:0;z-index:70;background:rgba(0,0,0,.55);place-items:center;padding:20px">
  <div class="lead-panel" style="max-width:480px;width:100%;position:relative">
    <button class="icon-btn" data-close aria-label="Close" style="position:absolute;right:12px;top:12px">✕</button>
    <span class="eyebrow">Before you go</span>
    <h3>Get the free 7-Day Breakup Reset</h3>
    <p class="muted">One short email a day for a week. Practical, not preachy. Unsubscribe any time.</p>
    <form class="form" data-form="Newsletter (exit)"><input type="hidden" name="_gotcha"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><button class="btn btn-grad btn-block" type="submit">Send me day 1</button></form>
    <div class="form-success">Check your inbox — day 1 is on its way.</div>
  </div>
</div>
<script src="{base}assets/js/main.js" defer></script>
{{extra_scripts}}
</body>
</html>
"""


def ad(kind="in-article", label="Advertisement"):
    fmt = {"leaderboard": "horizontal", "rect": "rectangle", "in-article": "fluid", "sky": "vertical"}[kind]
    return f'<div class="ad-slot {kind}" aria-label="{label}"><ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="0000000000" data-ad-format="{fmt}" data-full-width-responsive="true"></ins><span>{label}</span></div>'


def render(p):
    depth = p["path"].count("/")
    body = p["body"].replace("{ad:leaderboard}", ad("leaderboard")).replace("{ad:rect}", ad("rect")).replace("{ad:in-article}", ad("in-article")).replace("{ad:sky}", ad("sky"))
    scripts = "".join(f'<script src="{"../" * depth}assets/js/{s}" defer></script>' for s in p.get("scripts", []))
    out = head(p, depth) + body + footer(depth).replace("{extra_scripts}", scripts)
    out = out.replace("{base}", "../" * depth)
    dest = os.path.join(ROOT, p["path"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)
    return p["path"]


def sitemap(paths):
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE}/{'' if p == 'index.html' else p}</loc><lastmod>{today}</lastmod><changefreq>{'daily' if p in ('index.html', 'articles.html') else 'weekly'}</changefreq><priority>{'1.0' if p == 'index.html' else '0.7'}</priority></url>" for p in paths if not p.startswith("404"))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')


def main():
    written = []
    all_pages = pages.PAGES + articles.article_pages()
    # inject article cards into the guides hub and homepage
    cards = articles.cards(limit=None)
    for p in all_pages:
        p["body"] = p["body"].replace("{article-cards}", cards).replace("{article-cards-3}", articles.cards(limit=3)).replace("{article-cards-6}", articles.cards(limit=6))
        written.append(render(p))
    sitemap(written)
    print(f"built {len(written)} pages")


if __name__ == "__main__":
    main()
