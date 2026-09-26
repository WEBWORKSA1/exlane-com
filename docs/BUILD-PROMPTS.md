# ExLane.com — Phase-wise Build Prompts

These are the prompts used (and reusable) to build, extend and operate ExLane.com. Each phase is self-contained: paste it into an AI coding assistant or hand it to a developer. Constraints that apply to **every** phase are listed first.

## Global constraints (apply to every phase)

```
Project: ExLane.com — "The fast lane past your ex." A breakup-recovery publication with
free browser-side tools, evidence-informed guides, curated video, community stories,
coaching lead-generation, donations, contests, careers and advertiser/sponsor pages.

Hard rules:
1. Static site only (HTML/CSS/vanilla JS). Must deploy on GitHub Pages free plan
   (no server, no build service required at deploy time). Generator: python3 tools/build.py.
2. Every page shows, at the very top, the bar:
   "contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership"
   linking to https://web.works/contact.
3. The site has exactly one contact address. It must NEVER appear in plain text anywhere
   in HTML, JS, CSS, JSON, XML, sitemap, README or commit messages. It is stored base64-encoded
   in assets/js/main.js (CONFIG.k) and assembled only at click/submit time. Every form and
   "email us" link routes through that mechanism (or CONFIG.endpoint when set).
4. Trademark hygiene: never claim affiliation with any "Exlane/Ex Lane/Everlane/Express
   Lane/Exlan/OpenLane" mark; keep disclaimer.html's trademark notice on the site; no third-party
   logos; original name/logo only.
5. Monetization surfaces stay intact: AdSense units (leaderboard, in-article, rectangle, sky),
   ads.txt, YouTube embeds (youtube-nocookie facade), lead-gen forms, donations, sponsorship page.
6. Sensitive-topic UX: crisis resources in the footer, quick-exit button (Esc twice), no
   "get your ex back" manipulation content, tools store data only in localStorage.
7. Responsive (390px to 1440px+), dark mode via [data-theme], WCAG-AA contrast, semantic HTML,
   canonical + OG + JSON-LD on every page, sitemap.xml, robots.txt, 404.html.
```

---

## Phase 0 — Positioning & niche validation

```
Evaluate the domain ExLane.com. Enumerate every plausible reading of the name (ex-partner lane,
exit lane, express lane, expressway). For each: estimated monthly English search demand for the
core keyword cluster, AdSense CPM range, affiliate/lead-gen payout ranges, YouTube fit, donation
credibility, and trademark collision risk (search USPTO/Justia/EUIPO for exact and near marks).
Pick ONE niche with numbers and a one-paragraph rationale, list rejected options with the reason,
and write the trademark disclosure paragraph for disclaimer.html.
Deliverable: docs/RESEARCH.md §1.
```

## Phase 1 — Competitive research (35+ sites)

```
Visit at least 35 world-class sites across three clusters: (a) breakup/relationship advice,
(b) mental-wellness/therapy marketplaces/nonprofits, (c) lifestyle media & UGC communities.
For each capture: positioning, nav/IA, content formats, monetization (ad slot positions, affiliate,
courses, coaching, donations), lead-gen mechanics and form fields, design/UX patterns, trust
signals, and 2–3 features worth copying. Finish with cross-site patterns: top 15 recurring
features/forms/CTAs and top 10 monetization tactics. Flag any site that blocked fetching.
Deliverable: docs/RESEARCH.md §2–§4.
```

## Phase 2 — Information architecture & design system

```
From the research, define the sitemap (Home, Start Here, Quiz, Tools, Guides hub + 8 cornerstone
guides, Videos, Stories, Coaching (lead-gen), Support/Donate, Contests, Careers/Talent,
Advertise/Sponsor/Partner, About, Contact, Privacy, Terms, Disclaimer/Trademark, 404).
Create a design system in one CSS file: tokens (coral #e8563f, violet #6d4be6, teal #17b39b,
gold accent), Inter + Sora type scale, 18px radius cards, sticky glass header, notice bar, buttons
(primary/grad/outline/ghost/teal/gold), cards, steps, forms, chips, progress ring, calendar grid,
ad-slot placeholders, article layout with sticky sidebar, video facade, testimonial slider, tiers,
FAQ accordions, CTA band, footer with crisis box, sticky mobile CTA, quick-exit button,
dark-mode overrides, reduced-motion support.
Deliverable: assets/css/style.css
```

## Phase 3 — Static generator & shared shell

```
Write tools/build.py (stdlib only): page dicts → HTML. Shared head (meta/OG/canonical/JSON-LD/
fonts/AdSense loader/theme bootstrap), notice bar, header with nav + theme toggle + "Get Matched"
CTA + hamburger, footer (recover/community/company/legal columns, crisis resources, trademark
line), sticky mobile CTA, quick-exit, exit-intent newsletter modal, script injection per page,
{ad:*} token expansion, {base} relative-path expansion (site must work under /repo-name/ on
github.io and at the root of a custom domain), sitemap.xml generation.
Write assets/js/main.js: theme, nav, reveal-on-scroll (must degrade to visible), hidden-address
contact routing, generic data-form handler (mailto fallback / fetch to CONFIG.endpoint), chips,
YouTube facade, quick exit, share buttons, exit-intent.
Deliverables: tools/build.py, assets/js/main.js
```

## Phase 4 — Interactive tools (the retention engine)

```
Build assets/js/tools.js with six localStorage-only tools on tools.html:
1 No-Contact Tracker (start date, goal 30/60/90, day count, progress ring, stage messages,
  relapse log + restart); 2 Urge SOS (10-minute countdown, grounding step per minute, usage
  count); 3 30-Day Glow-Up Challenge (30 tasks, calendar grid, done toggles, progress bar,
  today highlight); 4 Journal (rotating expressive-writing prompts, save/list/delete entries);
  5 Reasons List (add/remove); 6 Unsent closure-letter generator (4 prompts → letter, copy).
Plus "erase all" control. No network calls. Accessible labels on every control.
Deliverables: tools.html section markup (tools/pages.py), assets/js/tools.js
```

## Phase 5 — Quiz (lead magnet #1)

```
Build "Are You Over Your Ex?" on quiz.html: 10 questions × 4 weighted answers (0–3), progress
bar, score /30, four bands (Green 0–6, Yellow 7–13, Amber 14–21, Red 22–30) each with title,
stage tag, 60–90 word interpretation and a stage-specific CTA; result panel contains an email
capture form pre-filled with the hidden quiz_result field; retake button; result cached in
localStorage. Disclaimer: self-reflection tool, not clinical.
Deliverables: quiz.html markup, assets/js/quiz.js
```

## Phase 6 — Cornerstone content (SEO engine)

```
Write 8 guides, 1,200–2,000 words each, research-referenced, no fluff, each with TOC, H2/H3s,
one in-article ad slot, callouts, internal links to tools/quiz/coaching, share row, and a
workbook-download lead form: The No-Contact Rule (30-day guide); How to Get Over an Ex
(7-stage roadmap); Why Breakups Physically Hurt; How to Stop Checking Your Ex's Social Media;
The Breakup Glow-Up 30-Day Plan; Should You Get Back Together? (decision framework);
Dating Again After Heartbreak; What to Text After a Breakup (scripts).
Guides hub with tag filters. Article JSON-LD. Sidebar: rect ad, quiz card, tools list, related,
coaching card, sky ad.
Deliverables: tools/articles.py, articles/*.html, articles.html
```

## Phase 7 — Monetization surfaces

```
AdSense: loader in head with client id constant, ins units in every {ad:*} slot, ads.txt.
Video: videos.html with playlist embed + featured grid using youtube-nocookie facades (no load
until click); creator-submission CTA. Lead-gen: coaching.html hero + multi-field match form
(timing, length, needs chips, format, budget, consent), how-it-works, FAQ, testimonials;
same form embedded on the homepage. Donations: donate.html with one-time amounts, monthly
Lane-Keeper tier, sponsor-a-prize, where-the-money-goes table, non-charity disclosure.
Sponsorship: advertise.html with audience stats, six offer cards, what-we-don't-run, media-kit
request form. Contests: contests.html with three programs, entry form, rules summary.
Careers: careers.html with open roles, coach/therapist partner listing, application form.
Deliverables: pages listed, updated pages.py
```

## Phase 8 — Legal, trust & safety

```
privacy.html (localStorage-only tools, email-delivered forms, AdSense cookie disclosure with
opt-out links, YouTube nocookie, GDPR/CCPA rights), terms.html (not-advice, referral disclosure,
submission licence, contest rules, acceptable use), disclaimer.html (trademark & copyright
notice naming near-marks and denying affiliation, medical disclaimer, affiliate disclosure,
video/story disclaimers), footer crisis resources, quick-exit.
```

## Phase 9 — QA

```
Automated: build; grep the whole tree for the plaintext contact address (must be zero hits);
verify every internal href/src and #anchor resolves; verify the notice bar is in every HTML
file; Playwright at 390×844 and 1366×900 for 8 key pages: no page errors, no console errors,
no horizontal overflow, quiz completes, tools respond, screenshots reviewed.
Manual: dark mode, keyboard nav, quick-exit, forms open mail client with correct subject/body.
```

## Phase 10 — Deploy

```
Repo: github.com/webworksa1/exlane-com, branch main, .nojekyll at root, built HTML committed.
GitHub Pages: Settings → Pages → Source "Deploy from a branch" → main / (root). Confirm the site
answers at https://webworksa1.github.io/exlane-com/. Optional CI: .github/workflows/pages.yml
(checkout → python3 tools/build.py → configure-pages → upload-pages-artifact → deploy-pages),
which needs a token with the "workflow" scope to push. For the custom domain: add a CNAME file
containing exlane.com, point A records to GitHub Pages IPs (185.199.108–111.153) and CNAME www →
webworksa1.github.io, enable "Enforce HTTPS".
```

## Phase 11 — Growth backlog (post-launch)

```
1. Replace mailto delivery with a form endpoint (CONFIG.endpoint) + ESP automation for the
   7-Day Reset, quiz-stage series and workbook PDF.
2. AdSense approval → real client id + slot ids; add Auto ads once traffic > 10k/mo.
3. Affiliate partners (therapy platforms, coaching networks) wired into coaching.html routing.
4. Publish 2 guides/week targeting long-tail ("no contact rule day 7", "ex texted me during
   no contact", "breakup insomnia").
5. ExLane YouTube channel: 60–90s explainers per guide; embed own videos first.
6. Community: stories moderation pipeline; comments via a static-friendly service.
7. Localization: ES, HI, FR, PT versions of the top 3 guides.
8. Custom domain + Search Console + GA4 + Bing Webmaster; monitor Core Web Vitals.
```
