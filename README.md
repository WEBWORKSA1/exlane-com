# ExLane.com — The fast lane past your ex

Breakup-recovery publication: free browser-side tools (no-contact tracker, urge SOS, 30-day challenge, journal, reasons list, unsent letter), a scored quiz, eight research-referenced guides, curated video, community stories, coaching lead-generation, donations, contests, careers and sponsorship pages.

Static HTML/CSS/JS. No framework, no build service. The finished pages are committed, so GitHub Pages (free plan) serves the repository root directly.

## Live

- GitHub Pages: https://webworksa1.github.io/exlane-com/
- Custom domain (when DNS is pointed): https://exlane.com

## Publishing

GitHub Pages was enabled automatically by the `gh-pages` branch (a copy of `main`). Two ways to keep it current:

- **Recommended (one click):** Settings → Pages → Source: *Deploy from a branch* → Branch: **main** / **(root)** → Save. From then on every push to `main` redeploys and `gh-pages` can be deleted.
- **Or** keep publishing from `gh-pages` by merging `main` into it after each change.

## Structure

```
index.html …          finished pages (generated — edit the sources below, rebuild, commit)
articles/*.html       eight cornerstone guides (generated)
assets/css/style.css  design system
assets/js/main.js     shell runtime: theme, nav, hidden-contact routing, forms, video facade, quick-exit
assets/js/tools.js    interactive tools (localStorage only)
assets/js/quiz.js     quiz logic
tools/build.py        generator (python3 tools/build.py) — writes *.html, articles/*.html, sitemap.xml
tools/pages.py        page content
tools/articles.py     guide content
docs/RESEARCH.md      niche decision + 40-site competitive research
docs/BUILD-PROMPTS.md phase-wise build prompts
ads.txt, robots.txt, sitemap.xml, site.webmanifest, 404.html, .nojekyll
```

## Editing

1. Change content in `tools/pages.py` or `tools/articles.py` (or styles/JS in `assets/`).
2. Run `python3 tools/build.py` (Python 3 standard library only).
3. Commit the regenerated HTML and push to `main` (then see Publishing above).

Optional CI build instead of committing HTML: add `.github/workflows/pages.yml` (checkout → `python3 tools/build.py` → `actions/configure-pages` → `actions/upload-pages-artifact` → `actions/deploy-pages`) and switch the Pages source to "GitHub Actions". Pushing workflow files needs a token with the `workflow` scope.

## Configuration checklist

| What | Where |
|---|---|
| AdSense publisher id | `ADSENSE_CLIENT` in `tools/build.py` **and** `ads.txt`; per-unit slot ids in `ad()` |
| Google Analytics | `GA_ID` in `tools/build.py` |
| Form delivery endpoint (Formspree/Basin/etc.) | `CONFIG.endpoint` in `assets/js/main.js` (until set, forms open the visitor's mail client with a pre-filled message) |
| Contact address | stored base64 in `CONFIG.k` in `assets/js/main.js`; never write it in plain text anywhere |
| Donation processor | replace the `data-contact` buttons on `donate.html` (pages.py) with PayPal / Stripe / Ko-fi links |
| Featured videos | `VIDEOS` and `PLAYLIST` in `tools/pages.py` |
| Custom domain | add a `CNAME` file containing `exlane.com`; DNS: A records 185.199.108.153 / 109.153 / 110.153 / 111.153, CNAME `www` → `webworksa1.github.io`; enable Enforce HTTPS |

## Rules baked into the site

- Top bar on every page: "contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership" → https://web.works/contact
- Single hidden contact address for all forms and inquiries.
- Trademark/copyright notice on `disclaimer.html`; ExLane is independent and unaffiliated with any similar mark.
- Crisis resources in the footer; quick-exit button (or press Esc twice) on every page.

## QA

A grep for the plaintext contact address across the tree must return nothing. Internal links, anchors and the notice bar are checked with the script in `docs/BUILD-PROMPTS.md` Phase 9; pages were rendered headlessly at 390px and 1366px with no JS errors and no horizontal overflow.
