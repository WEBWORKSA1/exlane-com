"""Page definitions for ExLane.com (everything except the guides, see articles.py).
{base} is replaced with the correct relative prefix at build time.
{ad:leaderboard} / {ad:rect} / {ad:in-article} / {ad:sky} become AdSense units."""

# Curated YouTube videos (ids sourced from public search listings; edit freely).
VIDEOS = [
    ("k0GQSJrpVhM", "How to fix a broken heart | Guy Winch | TED", "Science of heartbreak"),
    ("0lPqnOVk7WY", "The Ultimate Guide To The No Contact Rule", "No-contact"),
    ("xTlE0B_Z9Ik", "The No Contact Rule After A Breakup", "No-contact"),
    ("TmoRHJAZ9dc", "When Not To Use The No Contact Rule", "No-contact"),
    ("GrKtsMtPRZs", "Psychology of No Contact Rule on Dumper or Ex", "Psychology"),
    ("nmqcVSPKRSw", "When Is It Okay to Break the No Contact Rule?", "No-contact"),
]
PLAYLIST = "PLkTYN2Os0t9YRIN_3tRw1jNYYCjm3TSC7"


def video_card(vid, title, tag):
    return f"""<div class="card" style="padding:0;overflow:hidden"><div class="video" style="border-radius:0;box-shadow:none"><div class="video-facade" data-src="https://www.youtube-nocookie.com/embed/{vid}" data-title="{title}" role="button" tabindex="0" aria-label="Play: {title}"><div><div class="play">▶</div><b>{title}</b></div></div></div><div style="padding:14px 18px"><span class="tag tag-violet">{tag}</span></div></div>"""


VIDEO_GRID = "".join(video_card(*v) for v in VIDEOS)

TESTIMONIALS = [
    ("Priya, 29", "Day 41 of no-contact. The SOS timer stopped me from texting him at least six times. I didn't think a timer could do that."),
    ("Marcus, 34", "Took the quiz expecting 'you're fine'. Got 'amber'. It was right. Started the 30-day plan the same night."),
    ("Dani, 22", "The reasons list is the thing. Every time my brain rewrote the relationship, I read my own words back."),
    ("Tom, 41", "Divorce, two kids, shared house. The co-parenting version of no-contact in the guide is the only thing that worked."),
    ("Ayesha, 26", "I share my story here because reading other people's stories at 2 a.m. is what got me through week one."),
]
SLIDER = "".join(f'<div class="card"><p class="quote">“{q}”</p><div class="meta"><div class="avatar" style="width:32px;height:32px;font-size:.8rem">{n[0]}</div><b>{n}</b></div></div>' for n, q in TESTIMONIALS)

LEAD_FORM = """
<form class="form" data-form="Coach match request" id="match-form">
  <input type="hidden" name="_gotcha">
  <div class="form-row"><div><label for="m-name">First name</label><input id="m-name" name="first_name" required placeholder="Alex"></div><div><label for="m-email">Email</label><input id="m-email" type="email" name="email" required placeholder="you@example.com"></div></div>
  <div class="form-row"><div><label for="m-when">When did the breakup happen?</label><select id="m-when" name="breakup_timing"><option>Less than 2 weeks ago</option><option>2–6 weeks ago</option><option>1–3 months ago</option><option>3–12 months ago</option><option>Over a year ago</option><option>It's ongoing / on-off</option></select></div><div><label for="m-len">How long were you together?</label><select id="m-len" name="relationship_length"><option>Under 6 months</option><option>6–18 months</option><option>1.5–5 years</option><option>5+ years / married</option></select></div></div>
  <div><label>What do you need most right now? <span class="muted">(pick any)</span></label><div class="chips"><span class="chip">Stop contacting them</span><span class="chip">Decide whether to go back</span><span class="chip">Handle co-parenting</span><span class="chip">Sleep &amp; anxiety</span><span class="chip">Rebuild confidence</span><span class="chip">Dating again</span><span class="chip">Just talk to someone</span></div><input type="hidden" name="needs" data-chips></div>
  <div class="form-row"><div><label for="m-format">Preferred format</label><select id="m-format" name="format"><option>Video call</option><option>Phone</option><option>Text / chat coaching</option><option>Not sure yet</option></select></div><div><label for="m-budget">Budget per session</label><select id="m-budget" name="budget"><option>Free first call only</option><option>Under $50</option><option>$50–$100</option><option>$100–$200</option><option>$200+</option></select></div></div>
  <div><label for="m-msg">Anything the coach should know? <span class="muted">(optional)</span></label><textarea id="m-msg" name="message" placeholder="Two sentences is plenty."></textarea></div>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about coaching and to the <a href="{base}privacy.html">privacy policy</a>. I understand coaching is not therapy.</label>
  <button class="btn btn-grad btn-lg" type="submit">Match me with a coach →</button>
  <p class="form-note">Free 20-minute first call. No card required. Matched within 24 hours on business days.</p>
</form>
<div class="form-success"><b>Request received.</b> A coordinator will email you within 24 hours with two coach profiles and booking links. If you're in immediate distress, please use the crisis resources in the footer.</div>
"""

PAGES = []

# ------------------------------------------------------------------ HOME
PAGES.append({"path": "index.html", "title": "ExLane", "desc": "ExLane is the fast lane past your ex: a no-contact tracker, an 'are you over your ex' quiz, evidence-based guides, videos, real recovery stories and breakup coaching. Free tools, no sign-up.", "scripts": [], "jsonld": """<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"ExLane","url":"https://exlane.com/","description":"Breakup recovery tools, guides, videos and coaching.","potentialAction":{"@type":"SearchAction","target":"https://exlane.com/articles.html?q={search_term_string}","query-input":"required name=search_term_string"}}</script>""", "body": """
<section class="hero"><div class="lane-bg"></div><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Breakup recovery, without the fluff</span>
    <h1>The fast lane <span class="grad-text">past your ex.</span></h1>
    <p class="lead">Free no-contact tracker, a two-minute quiz that tells you where you actually are, guides built on what the research says works, and coaches when you need a human. No sign-up. Nothing leaves your browser.</p>
    <div class="hero-cta"><a class="btn btn-grad btn-lg" href="{base}quiz.html">Am I over my ex? (2-min quiz)</a><a class="btn btn-outline btn-lg" href="{base}tools.html">Start the no-contact tracker</a></div>
    <div class="hero-proof"><span><b>10</b> free tools</span><span><b>0</b> accounts required</span><span><b>30</b>-day plans</span><span><b>24h</b> coach matching</span></div>
  </div>
  <div class="hero-card reveal">
    <span class="tag tag-teal">Where are you today?</span>
    <h3 style="margin-top:10px">Pick your lane</h3>
    <div class="steps" style="margin-top:12px">
      <a class="step" href="{base}tools.html#sos" style="color:inherit"><div><h3>It just happened / I want to text them</h3><p class="muted small">Urge SOS: 10-minute timer + grounding steps.</p></div></a>
      <a class="step" href="{base}articles/no-contact-rule.html" style="color:inherit"><div><h3>I'm trying to stay no-contact</h3><p class="muted small">The 30-day protocol and the tracker.</p></div></a>
      <a class="step" href="{base}articles/should-you-get-back-together.html" style="color:inherit"><div><h3>I'm deciding whether to go back</h3><p class="muted small">A framework, not a feeling.</p></div></a>
      <a class="step" href="{base}articles/dating-again.html" style="color:inherit"><div><h3>I'm mostly fine and ready for what's next</h3><p class="muted small">Glow-up plan and the dating-again checklist.</p></div></a>
    </div>
  </div>
</div></section>

<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>

<section><div class="wrap">
  <div class="center" style="max-width:680px;margin:0 auto 36px"><span class="eyebrow">Tools</span><h2>Built for the moment your thumb hovers over their name</h2><p class="lead">Everything runs in your browser. No account, no data sent anywhere.</p></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="ico">⏱</div><h3>No-Contact Tracker</h3><p class="muted">Day counter, progress ring, relapse log and stage-specific messages for days 0–90.</p><a class="card-link" href="{base}tools.html#no-contact" aria-label="No-Contact Tracker"></a></div>
    <div class="card reveal"><div class="ico">🚨</div><h3>Urge SOS</h3><p class="muted">A 10-minute delay timer with grounding steps. Most urges pass in under seven.</p><a class="card-link" href="{base}tools.html#sos" aria-label="Urge SOS"></a></div>
    <div class="card reveal"><div class="ico">📅</div><h3>30-Day Glow-Up Challenge</h3><p class="muted">One concrete task a day across body, space, money, people and skills.</p><a class="card-link" href="{base}tools.html#glow" aria-label="30-Day Challenge"></a></div>
    <div class="card reveal"><div class="ico">📓</div><h3>Journal &amp; prompts</h3><p class="muted">Expressive-writing prompts shown to speed recovery. Private to your device.</p><a class="card-link" href="{base}tools.html#journal" aria-label="Journal"></a></div>
    <div class="card reveal"><div class="ico">📋</div><h3>Reasons List</h3><p class="muted">Your own words about why it ended, for when your brain rewrites the story.</p><a class="card-link" href="{base}tools.html#reasons" aria-label="Reasons list"></a></div>
    <div class="card reveal"><div class="ico">✉️</div><h3>Unsent Letter</h3><p class="muted">A guided closure letter you write and never send. Copy, keep, or delete.</p><a class="card-link" href="{base}tools.html#letter" aria-label="Closure letter"></a></div>
  </div>
</div></section>

<section style="background:var(--bg-3)"><div class="wrap">
  <div class="lead-split">
    <div><span class="eyebrow">The quiz</span><h2>Are you actually over your ex?</h2><p class="lead">Ten questions. A score out of 30, a stage (green, yellow, amber, red), and the one thing to do next. Takes two minutes; most people are surprised by the result.</p><a class="btn btn-primary btn-lg" href="{base}quiz.html">Take the quiz</a></div>
    <div class="card"><div class="stats" style="grid-template-columns:1fr 1fr"><div class="stat"><b>0–6</b>Green: through it</div><div class="stat"><b>7–13</b>Yellow: loose ends</div><div class="stat"><b>14–21</b>Amber: recovering</div><div class="stat"><b>22–30</b>Red: acute</div></div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:12px;margin-bottom:26px"><div><span class="eyebrow">Guides</span><h2 style="margin:0">What the research says works</h2></div><a class="btn btn-outline" href="{base}articles.html">All guides →</a></div>
  <div class="grid grid-3">{article-cards-6}</div>
</div></section>

<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>

<section style="background:var(--bg-3)"><div class="wrap">
  <div class="center" style="margin-bottom:30px"><span class="eyebrow">Watch</span><h2>Videos worth your time</h2><p class="muted">Curated talks and explainers. <a href="{base}videos.html">See the full library →</a></p></div>
  <div class="grid grid-3">""" + "".join(video_card(*v) for v in VIDEOS[:3]) + """</div>
</div></section>

<section><div class="wrap">
  <div class="center" style="margin-bottom:24px"><span class="eyebrow">Stories</span><h2>People who got through it</h2></div>
  <div class="slider">""" + SLIDER + """</div>
  <div class="center" style="margin-top:12px"><a class="btn btn-outline" href="{base}stories.html">Read more stories</a> <a class="btn btn-ghost" href="{base}stories.html#submit">Share yours →</a></div>
</div></section>

<section id="lead" style="background:var(--bg-3)"><div class="wrap">
  <div class="lead-split">
    <div><span class="eyebrow">Coaching</span><h2>When a tracker isn't enough, talk to someone who does this every day</h2>
      <ul class="bullets"><li>Free 20-minute first call, no card</li><li>Matched to a coach within 24 hours (business days)</li><li>Specialists in no-contact, co-parenting, on-off cycles and dating again</li><li>Licensed therapy referrals when coaching isn't the right fit</li></ul>
      <p class="muted small">Coaching is not therapy. If you're in crisis, use the resources in the footer.</p></div>
    <div class="lead-panel">""" + LEAD_FORM + """</div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="cta-band reveal"><h2>Get the free 7-Day Breakup Reset</h2><p>One short, practical email a day for a week. 40,000+ words of guides distilled into seven actions.</p>
    <form class="newsletter" data-form="Newsletter (home)"><input type="hidden" name="_gotcha"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><button class="btn" type="submit">Send day 1</button></form>
    <div class="form-success" style="max-width:520px;margin:14px auto 0">You're in. Day 1 lands in a few minutes.</div>
    <p class="small" style="margin-top:12px;opacity:.85">No spam, unsubscribe in one click.</p></div>
</div></section>

<section class="tight"><div class="wrap">
  <div class="trust-row"><span>Evidence-informed</span><span>·</span><span>No account required</span><span>·</span><span>Reader-supported</span><span>·</span><span>Quick-exit button on every page</span><span>·</span><span>Independent &amp; ad-transparent</span></div>
</div></section>
"""})

# ------------------------------------------------------------------ START HERE
PAGES.append({"path": "start-here.html", "title": "Start Here: Your Breakup Recovery Roadmap", "desc": "New to ExLane? Find your stage, pick the right tool, and follow a clear plan from the first 72 hours through to dating again.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Start here</span><h1>Your recovery roadmap</h1><p class="lead">Breakups are patterned. Find your stage below and use only what that stage needs. Everything else can wait.</p></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="steps">
  <div class="step"><div><h3>First 72 hours: stabilise</h3><p>Tell two people. Set your no-contact start date in the <a href="{base}tools.html#no-contact">tracker</a>. Mute their accounts. Use the <a href="{base}tools.html#sos">Urge SOS</a> when the texting urge hits. Eat, sleep, water. Make no decisions.</p></div></div>
  <div class="step"><div><h3>Week 1–2: withdrawal</h3><p>Read <a href="{base}articles/why-breakups-hurt.html">why it physically hurts</a> so you stop treating the pain as a message. Start the <a href="{base}tools.html#reasons">reasons list</a>. Follow the <a href="{base}articles/no-contact-rule.html">no-contact protocol</a>.</p></div></div>
  <div class="step"><div><h3>Week 2–4: break the loops</h3><p>The profile-checking loop: <a href="{base}articles/stop-checking-ex-social-media.html">this method</a>. Start journaling with the <a href="{base}tools.html#journal">prompts</a>. If you're deciding about going back, use the <a href="{base}articles/should-you-get-back-together.html">framework</a>, not the feeling.</p></div></div>
  <div class="step"><div><h3>Month 1–3: rebuild</h3><p>Begin the <a href="{base}tools.html#glow">30-Day Glow-Up Challenge</a>. Write the <a href="{base}tools.html#letter">unsent letter</a>. Consider a <a href="{base}coaching.html">coach</a> if you're stuck in stage 3 (bargaining) for more than a month.</p></div></div>
  <div class="step"><div><h3>Month 3+: next chapter</h3><p>Take the <a href="{base}quiz.html">quiz</a> again. When you're green, read <a href="{base}articles/dating-again.html">dating again</a>. Then <a href="{base}stories.html#submit">tell your story</a> for the person reading this at 2 a.m.</p></div></div>
</div>
<div class="divider"></div>
<div class="grid grid-2">
  <div class="card"><h3>Not sure which stage?</h3><p class="muted">The quiz scores ten answers and tells you.</p><a class="btn btn-primary" href="{base}quiz.html">Take the quiz</a></div>
  <div class="card"><h3>Need a human today?</h3><p class="muted">Free 20-minute first coaching call, matched within 24h.</p><a class="btn btn-outline" href="{base}coaching.html">Get matched</a></div>
</div>
</div></section>
"""})

# ------------------------------------------------------------------ QUIZ
PAGES.append({"path": "quiz.html", "title": "Are You Over Your Ex? The 2-Minute Quiz", "desc": "Ten questions, a score out of 30, and a clear stage: green, yellow, amber or red. Then the single most useful next step for your stage.", "scripts": ["quiz.js"], "body": """
<section class="page-head"><div class="wrap-narrow center"><span class="eyebrow">The quiz</span><h1>Are you over your ex?</h1><p class="lead">Answer honestly. Nobody sees this but you; the result isn't stored anywhere except your own browser.</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow">
<div class="tool" id="quiz">
  <div id="quiz-body">
    <div class="meta" style="justify-content:space-between"><span id="quiz-count">Question 1 of 10</span><span class="muted">≈ 2 minutes</span></div>
    <div class="progress" style="margin:10px 0 20px"><i id="quiz-bar"></i></div>
    <h2 id="quiz-q" style="font-size:1.4rem"></h2>
    <div class="quiz-opts" id="quiz-opts"></div>
  </div>
  <div class="result-box" id="quiz-result">
    <span class="tag" id="res-tag"></span>
    <div class="big-num" id="res-score" style="margin:10px 0"></div>
    <h2 id="res-title"></h2>
    <p class="lead" id="res-body"></p>
    <div class="lead-panel" style="margin-top:22px">
      <h3>Get your stage-specific plan by email</h3>
      <p class="muted small">A short series matched to your result, plus the printable workbook.</p>
      <form class="form" data-form="Quiz result plan request"><input type="hidden" name="_gotcha"><input type="hidden" name="quiz_result" id="res-stage">
        <div class="form-row"><input type="text" name="first_name" placeholder="First name" aria-label="First name" required><input type="email" name="email" placeholder="Email" aria-label="Email" required></div>
        <button class="btn btn-grad btn-block" type="submit" id="res-cta">Send my plan</button>
      </form>
      <div class="form-success">Sent. Check your inbox in a few minutes.</div>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn btn-outline" href="{base}tools.html">Open the tools</a><a class="btn btn-outline" href="{base}coaching.html">Talk to a coach</a><button class="btn btn-ghost" type="button" id="quiz-restart">Retake</button></div>
  </div>
</div>
<p class="muted small center" style="margin-top:16px">This quiz is a self-reflection tool, not a clinical assessment.</p>
{ad:in-article}
</div></section>
"""})

# ------------------------------------------------------------------ TOOLS
PAGES.append({"path": "tools.html", "title": "Free Breakup Recovery Tools: No-Contact Tracker, Urge SOS, 30-Day Challenge", "desc": "Interactive breakup recovery tools that run entirely in your browser: no-contact day counter, urge SOS timer, 30-day glow-up challenge, journal prompts, reasons list and closure-letter generator.", "scripts": ["tools.js"], "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Tools</span><h1>Recovery tools that live in your browser</h1><p class="lead">No account. No server. Everything below is saved only on this device (you can <button class="btn btn-sm btn-ghost" id="erase-all" type="button">erase it all</button> any time).</p>
<div class="pill-row"><a class="chip" href="#no-contact">No-Contact Tracker</a><a class="chip" href="#sos">Urge SOS</a><a class="chip" href="#glow">30-Day Challenge</a><a class="chip" href="#journal">Journal</a><a class="chip" href="#reasons">Reasons List</a><a class="chip" href="#letter">Unsent Letter</a></div></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>

<section id="no-contact" style="padding-top:10px"><div class="wrap"><div class="tool" id="nc-tool">
  <div class="two-col">
    <div><span class="tag tag-brand">Tool 1</span><h2 style="margin-top:10px">No-Contact Tracker</h2><p class="muted">Set the date you went no-contact. The counter, the ring and the message update daily. If you slip, hit reset: the old streak is logged as a relapse, not erased.</p>
      <div class="form-row"><div><label for="nc-date">No-contact start date</label><input type="date" id="nc-date"></div><div><label for="nc-goal">Goal</label><select id="nc-goal"><option value="30">30 days</option><option value="60">60 days</option><option value="90">90 days</option></select></div></div>
      <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap"><button class="btn btn-outline btn-sm" id="nc-reset" type="button">I slipped — restart today</button><span class="muted small" style="align-self:center">Relapses logged: <b id="nc-relapses">0</b></span></div></div>
    <div class="center"><div class="big-num" id="nc-days">—</div><div class="muted" style="margin-bottom:16px">days no-contact</div><div class="ring" id="nc-ring"><div id="nc-ring-text">0%</div></div><p id="nc-msg" style="margin-top:16px;font-weight:600"></p></div>
  </div>
</div></div></section>

<section id="sos" style="padding-top:0"><div class="wrap"><div class="tool sos">
  <div class="two-col">
    <div><span class="tag" style="background:rgba(255,255,255,.2);color:#fff">Tool 2</span><h2 style="margin-top:10px">Urge SOS: 10 minutes before you text</h2><p>You don't have to not-text them forever. You have to not-text them for the next ten minutes. Start the timer; a grounding step appears every minute. Urges used: <b id="sos-count">0</b>.</p><button class="btn btn-lg" id="sos-start" type="button">Start 10-minute delay</button></div>
    <div class="center"><div class="big-num" id="sos-timer" style="background:#fff;-webkit-background-clip:text;background-clip:text">10:00</div><p id="sos-step" style="font-weight:600;font-size:1.1rem;min-height:3.4em;margin-top:14px">Press start when your thumb is hovering over their name.</p></div>
  </div>
</div></div></section>

<section id="glow" style="padding-top:0"><div class="wrap"><div class="tool">
  <span class="tag tag-teal">Tool 3</span><h2 style="margin-top:10px">30-Day Glow-Up Challenge</h2><p class="muted">One concrete task a day across body, space, money, people and skills. Tap a day to see the task; mark it done. <a href="{base}articles/glow-up-plan.html">Read the plan behind it.</a></p>
  <div class="progress" style="margin:14px 0"><i id="glow-progress"></i></div><p class="small muted"><b id="glow-count">0</b> / 30 complete</p>
  <div class="calendar" id="glow-cal"></div>
  <div class="card" style="margin-top:18px"><p id="glow-task" style="font-weight:600;font-size:1.1rem"></p><button class="btn btn-teal" id="glow-toggle" type="button">Mark done</button></div>
</div></div></section>

<section class="tight"><div class="wrap">{ad:in-article}</div></section>

<section id="journal" style="padding-top:0"><div class="wrap"><div class="tool">
  <div class="two-col">
    <div><span class="tag tag-violet">Tool 4</span><h2 style="margin-top:10px">Journal prompts</h2><p class="muted">Expressive writing about a breakup, 15 minutes a few times a week, measurably reduces rumination. Prompts rotate; entries stay on this device.</p><div class="journal-prompt" id="journal-prompt"></div><button class="btn btn-outline btn-sm" id="journal-next" type="button">Another prompt</button></div>
    <div><label for="journal-text">Your entry</label><textarea id="journal-text" placeholder="Write freely. Nobody reads this."></textarea><div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap"><button class="btn btn-primary" id="journal-save" type="button">Save entry</button><button class="btn btn-ghost btn-sm" id="journal-clear" type="button">Delete all</button></div><p class="small muted" style="margin-top:12px">Entries on this device: <b id="journal-n">0</b></p><ul id="journal-list" class="small" style="padding-left:18px"></ul></div>
  </div>
</div></div></section>

<section id="reasons" style="padding-top:0"><div class="wrap"><div class="tool">
  <span class="tag tag-brand">Tool 5</span><h2 style="margin-top:10px">Reasons List</h2><p class="muted">Idealisation is the main engine of relapse. Write, in your own words, why it ended and what wasn't working. Read it when the story starts rewriting itself.</p>
  <form id="reasons-form" class="newsletter" style="margin:0;max-width:640px"><input id="reason-input" placeholder="e.g. I was always the one apologising" aria-label="Add a reason"><button class="btn btn-primary" type="submit">Add</button></form>
  <ol id="reasons-list" style="margin-top:16px"></ol>
</div></div></section>

<section id="letter" style="padding-top:0"><div class="wrap"><div class="tool">
  <div class="two-col">
    <div><span class="tag tag-violet">Tool 6</span><h2 style="margin-top:10px">Unsent closure letter</h2><p class="muted">Closure is something you give yourself. Fill in four prompts; a letter is assembled that you can keep, print, or delete. Never send it.</p>
      <form id="letter-form" class="form"><div><label for="l-name">Their name (or a placeholder)</label><input id="l-name" name="name"></div><div><label for="l-g">I'm grateful for…</label><input id="l-g" name="grateful"></div><div><label for="l-h">What hurt was…</label><input id="l-h" name="hurt"></div><div><label for="l-l">What I learned…</label><input id="l-l" name="lesson"></div><div><label for="l-f">Where I'm going…</label><input id="l-f" name="future"></div><button class="btn btn-grad" type="submit">Write my letter</button></form></div>
    <div><label for="letter-out">Your letter</label><textarea id="letter-out" style="min-height:320px" readonly></textarea><button class="btn btn-outline btn-sm" id="letter-copy" type="button" style="margin-top:10px">Copy</button></div>
  </div>
</div></div></section>

<section style="padding-top:0"><div class="wrap"><div class="cta-band"><h2>Want these as a printable workbook?</h2><p>Tracker, reasons list, 30-day plan and the letter template as one PDF.</p><form class="newsletter" data-form="Workbook download (tools page)"><input type="hidden" name="_gotcha"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><button class="btn" type="submit">Email me the workbook</button></form><div class="form-success" style="max-width:520px;margin:14px auto 0">Sent. Check your inbox.</div></div></div></section>
"""})

# ------------------------------------------------------------------ GUIDES HUB
PAGES.append({"path": "articles.html", "title": "Breakup Recovery Guides", "desc": "Evidence-informed guides on the no-contact rule, getting over an ex, the science of heartbreak, social-media habits, the glow-up plan, getting back together, dating again and what to text.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Guides</span><h1>Breakup recovery guides</h1><p class="lead">Long-form, practical, and written against the research rather than vibes. Start with the no-contact rule if you're new.</p>
<div class="pill-row" id="filters"><button class="chip active" type="button" data-f="all">All</button><button class="chip" type="button" data-f="No-Contact">No-contact</button><button class="chip" type="button" data-f="Roadmap">Roadmap</button><button class="chip" type="button" data-f="Science">Science</button><button class="chip" type="button" data-f="Habits">Habits</button><button class="chip" type="button" data-f="Rebuild">Rebuild</button><button class="chip" type="button" data-f="Decisions">Decisions</button><button class="chip" type="button" data-f="Next chapter">Next chapter</button><button class="chip" type="button" data-f="Scripts">Scripts</button></div></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="grid grid-3" id="guide-grid">{article-cards}</div>
<script>document.addEventListener('click',function(e){var b=e.target.closest('#filters .chip');if(!b)return;document.querySelectorAll('#filters .chip').forEach(function(x){x.classList.remove('active')});b.classList.add('active');var f=b.dataset.f;document.querySelectorAll('#guide-grid .post').forEach(function(c){var t=c.querySelector('.tag').textContent.trim();c.style.display=(f==='all'||t===f)?'':'none'})});</script>
<div class="divider"></div>
<div class="lead-panel"><div class="lead-split"><div><span class="eyebrow">Newsletter</span><h3>New guides, one email a week</h3><p class="muted">Plus the free 7-Day Breakup Reset when you join.</p></div><form class="form" data-form="Newsletter (guides)"><input type="hidden" name="_gotcha"><div class="form-row"><input type="text" name="first_name" placeholder="First name" aria-label="First name"><input type="email" name="email" placeholder="Email" aria-label="Email" required></div><button class="btn btn-grad" type="submit">Subscribe</button></form><div class="form-success">Subscribed. Welcome.</div></div></div>
</div></section>
"""})

# ------------------------------------------------------------------ VIDEOS
PAGES.append({"path": "videos.html", "title": "Breakup Recovery Videos", "desc": "Curated talks and explainers on heartbreak, the no-contact rule and moving on, plus the ExLane channel.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Videos</span><h1>Watch: the best of breakup recovery on video</h1><p class="lead">Curated from public channels; videos load only when you press play (no tracking until then).</p></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="video reveal"><div class="video-facade" data-src="https://www.youtube-nocookie.com/embed/videoseries?list=""" + PLAYLIST + """" data-title="No Contact Rule playlist" role="button" tabindex="0"><div><div class="play">▶</div><b style="font-size:1.3rem">No-Contact Rule: full playlist</b><p class="small" style="opacity:.85">Public YouTube playlist · plays inside this page</p></div></div></div>
  <h2 style="margin-top:40px">Featured</h2>
  <div class="grid grid-3">""" + VIDEO_GRID + """</div>
  {ad:in-article}
  <div class="grid grid-2" style="margin-top:30px">
    <div class="card card-feature"><h3>Want your video featured here?</h3><p>We feature creators whose work matches the evidence. Coaches, therapists, and people with a story: send a link.</p><a class="btn" style="background:#fff;color:var(--brand-2)" href="{base}advertise.html#creators">Submit a video</a></div>
    <div class="card"><h3>ExLane on YouTube</h3><p class="muted">Short explainers of each guide, tool walk-throughs and story readings. Subscribe so you don't miss the 7-Day Reset series.</p><a class="btn btn-primary" href="https://www.youtube.com/results?search_query=exlane+breakup+recovery" rel="noopener" target="_blank">Find the channel</a></div>
  </div>
</div></section>
"""})

# ------------------------------------------------------------------ STORIES
PAGES.append({"path": "stories.html", "title": "Recovery Stories From Real People", "desc": "First-person breakup recovery stories: what happened, what helped, what they'd tell you at 2 a.m. Share yours anonymously.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Stories</span><h1>Stories from the other side</h1><p class="lead">Reading someone else's day 40 when you're on day 4 is the closest thing to proof that it ends. Names changed on request; stories lightly edited.</p></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="pill-row" style="margin-bottom:22px"><span class="chip active">All</span><span class="chip">Just broke up</span><span class="chip">No-contact</span><span class="chip">Divorce &amp; co-parenting</span><span class="chip">Got back together (and left again)</span><span class="chip">Dating again</span><span class="chip">Success story</span></div>
  <div class="grid grid-2">
    <article class="card"><span class="tag tag-brand">No-contact</span><h3 style="margin-top:10px">"Day 41. The timer stopped six texts."</h3><p class="muted">Priya, 29 · 3-year relationship · ended by him</p><p>The first week I wrote him a message every night and deleted it. Then I found the SOS timer and used it like a life raft. The urge is real, but it's ten minutes long. That's the whole secret nobody told me. By day 20 I was using it once a week. By day 41 I forgot to check the counter for two days and that's when I knew.</p><p class="small muted">What helped most: the timer, and telling my sister to never give me updates.</p></article>
    <article class="card"><span class="tag tag-violet">Divorce &amp; co-parenting</span><h3 style="margin-top:10px">"Two kids, one house, zero contact was impossible. Grey rock wasn't."</h3><p class="muted">Tom, 41 · 12-year marriage</p><p>Everyone said no-contact and I laughed; we had a school run. What worked was the co-parenting version: a shared calendar app, written messages only, child logistics only, one line each. I stopped explaining myself. Six months later I realised I hadn't thought about what she was feeling in weeks. That's recovery when you can't disappear.</p><p class="small muted">What helped most: the reasons list, re-read every Sunday night.</p></article>
    <article class="card"><span class="tag tag-teal">Got back together (and left again)</span><h3 style="margin-top:10px">"Third reunion. The framework said no, and it was right."</h3><p class="muted">Dani, 22 · on-off for 2 years</p><p>I read the decision framework as a formality, expecting it to give me permission. It asked whether the reason it ended had specifically changed. It hadn't. It asked whether the conversations only happened late at night. They did. I cried, and then I didn't go back, and three months later I'm writing this from a life that's mine.</p><p class="small muted">What helped most: the 30-day test question: "what would I tell a friend?"</p></article>
    <article class="card"><span class="tag tag-teal">Success story</span><h3 style="margin-top:10px">"Green on the quiz, 14 months later. It took what it took."</h3><p class="muted">Marcus, 34 · 6-year relationship</p><p>I took the quiz at month two and got red. I didn't believe it. Took it at month five: amber. Month nine: yellow. Last week: green. I don't think there was one thing. It was no-contact plus lifting plus letting friends drag me out plus one coach session where I finally said the thing out loud. Time only works if you fill it.</p><p class="small muted">What helped most: the glow-up challenge, twice through.</p></article>
  </div>
  {ad:in-article}
  <div class="lead-panel" id="submit" style="margin-top:34px">
    <div class="lead-split">
      <div><span class="eyebrow">Share your story</span><h2>Tell the person on day 4 what day 40 looks like</h2><ul class="bullets"><li>Anonymous by default; we never publish contact details</li><li>Lightly edited for length and privacy</li><li>Selected stories are read on the ExLane channel and entered into the monthly <a href="{base}contests.html">story contest</a></li></ul></div>
      <form class="form" data-form="Story submission"><input type="hidden" name="_gotcha">
        <div class="form-row"><div><label for="s-name">Name to publish <span class="muted">(or "Anonymous")</span></label><input id="s-name" name="display_name" required></div><div><label for="s-email">Email <span class="muted">(never published)</span></label><input id="s-email" type="email" name="email" required></div></div>
        <div class="form-row"><div><label for="s-cat">Category</label><select id="s-cat" name="category"><option>Just broke up</option><option>No-contact</option><option>Divorce &amp; co-parenting</option><option>Got back together (and left again)</option><option>Dating again</option><option>Success story</option></select></div><div><label for="s-age">Age &amp; relationship length <span class="muted">(optional)</span></label><input id="s-age" name="age_and_length" placeholder="29, 3 years"></div></div>
        <div><label for="s-story">Your story <span class="muted">(150–800 words)</span></label><textarea id="s-story" name="story" required minlength="150" style="min-height:180px"></textarea></div>
        <div><label for="s-help">What helped most?</label><input id="s-help" name="what_helped"></div>
        <label class="check"><input type="checkbox" name="consent" value="yes" required> I'm over 18, this is my own story, and ExLane may publish and edit it under the <a href="{base}terms.html">terms</a>.</label>
        <label class="check"><input type="checkbox" name="contest" value="yes"> Enter it in this month's story contest.</label>
        <button class="btn btn-grad" type="submit">Submit my story</button>
      </form>
      <div class="form-success">Thank you. We read every submission and reply within a week if we'd like to publish it.</div>
    </div>
  </div>
</div></section>
"""})

# ------------------------------------------------------------------ COACHING (LEAD GEN)
PAGES.append({"path": "coaching.html", "title": "Breakup Coaching: Get Matched in 24 Hours", "desc": "Get matched with a breakup coach within 24 hours. Free 20-minute first call. Specialists in no-contact, co-parenting, on-off cycles and dating again. Licensed therapy referrals available.", "body": """
<section class="hero" style="padding-bottom:20px"><div class="lane-bg"></div><div class="wrap hero-grid">
  <div><span class="eyebrow">Coaching</span><h1>Talk to someone who does this every day</h1><p class="lead">A breakup coach is not a therapist and not your friend. They're the person who has watched a thousand people go through exactly this and knows which step you're skipping.</p>
    <div class="hero-proof" style="margin-top:10px"><span><b>Free</b> first 20 min</span><span><b>24h</b> matching</span><span><b>No card</b> required</span><span><b>Text, phone or video</b></span></div>
    <div class="divider"></div>
    <h3>Who this is for</h3><ul class="bullets"><li>You keep breaking no-contact and can't figure out why</li><li>You're stuck deciding whether to go back</li><li>Co-parenting or a shared workplace makes "just block them" impossible</li><li>You're "fine" but you haven't dated in two years</li><li>You need a plan and someone to report back to</li></ul>
    <h3>Who this is not for</h3><p class="muted">If you're experiencing thoughts of self-harm, can't function at work, or there was abuse, you need a licensed professional. Tick "licensed therapy referral" below and we'll route you to vetted options instead.</p></div>
  <div class="lead-panel reveal"><span class="eyebrow">Step 1 of 1</span><h3>Get matched</h3>""" + LEAD_FORM.replace('<option>Not sure yet</option>', '<option>Not sure yet</option><option>Licensed therapy referral instead</option>') + """</div>
</div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2 class="center">How it works</h2>
  <div class="grid grid-4">
    <div class="card"><div class="ico">1</div><h3>Tell us where you are</h3><p class="muted">The form above. Two minutes.</p></div>
    <div class="card"><div class="ico">2</div><h3>We match</h3><p class="muted">Two coach profiles within 24 hours, chosen for your situation, format and budget.</p></div>
    <div class="card"><div class="ico">3</div><h3>Free first call</h3><p class="muted">20 minutes. You decide if it's a fit. No pressure, no card.</p></div>
    <div class="card"><div class="ico">4</div><h3>Work the plan</h3><p class="muted">Weekly or fortnightly sessions plus text check-ins. Most people need 4–8.</p></div>
  </div>
  <div class="divider"></div>
  <h2 class="center">Common questions</h2>
  <div class="wrap-narrow">
    <details><summary>What's the difference between a coach and a therapist?</summary><p>Therapists are licensed clinicians who diagnose and treat mental-health conditions. Coaches are not licensed and don't treat conditions; they help you set and follow a plan. If you're unsure which you need, say so in the form and we'll route you honestly.</p></details>
    <details><summary>How much does coaching cost?</summary><p>The first 20 minutes are free. After that, coaches on our list charge between roughly $40 and $200 per session depending on experience and format. You choose your budget band in the form and we only match within it.</p></details>
    <details><summary>Is this confidential?</summary><p>Your form goes only to the matching coordinator and the coaches you're matched with. We never sell or share the list. See the <a href="{base}privacy.html">privacy policy</a>.</p></details>
    <details><summary>Does ExLane get paid?</summary><p>Yes: coaches and therapy platforms pay us a referral fee when you book. That's part of how the free tools stay free. It doesn't change who we match you with; we drop coaches with poor feedback regardless of fee.</p></details>
    <details><summary>Are you a coach who wants to be listed?</summary><p>Apply on the <a href="{base}careers.html#coaches">talent page</a>. We check credentials, insurance, and references, and we watch client feedback.</p></details>
  </div>
  <div class="divider"></div>
  <div class="slider">""" + SLIDER + """</div>
</div></section>
"""})

# ------------------------------------------------------------------ DONATE / SUPPORT
PAGES.append({"path": "donate.html", "title": "Support ExLane", "desc": "ExLane's tools are free and account-free. Reader support pays for hosting, editorial, contest prizes, and keeping the site light on ads. One-time or monthly.", "body": """
<section class="page-head"><div class="wrap-narrow center"><span class="eyebrow">Support us</span><h1>Keep the lane open</h1><p class="lead">Every tool on ExLane is free, needs no account, and sends nothing to a server. That costs money to run and write. If it helped, this is how you pay it forward to the next person on day 1.</p></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="tiers">
    <div class="card tier"><h3>One-time</h3><div class="price">Any amount</div><p class="muted">Buy the editors a coffee, or fund one story-contest prize.</p>
      <div class="amounts"><span class="chip">$5</span><span class="chip active">$15</span><span class="chip">$30</span><span class="chip">$100</span></div>
      <a class="btn btn-primary btn-block" style="margin-top:14px" href="#" data-contact data-subject="One-time support for ExLane">Donate once</a><p class="form-note" style="margin-top:8px">Card, PayPal and bank options sent by reply. Buttons connect to your processor once configured (see README).</p></div>
    <div class="card tier pop"><span class="tag tag-violet">Most helpful</span><h3 style="margin-top:8px">Monthly Lane-Keeper</h3><div class="price">$7<span class="muted" style="font-size:1rem">/mo</span></div><p class="muted">Predictable support. Name in the supporters list (optional), early access to new tools, and a vote on the next guide topic.</p><a class="btn btn-grad btn-block" href="#" data-contact data-subject="Monthly Lane-Keeper support">Become a Lane-Keeper</a></div>
    <div class="card tier"><h3>Sponsor a prize</h3><div class="price">$250+</div><p class="muted">Fund a month of the story contest or the glow-up challenge prize. Your name or brand on the contest page.</p><a class="btn btn-outline btn-block" href="{base}advertise.html#sponsor">Sponsor</a></div>
  </div>
  <div class="divider"></div>
  <div class="grid grid-2">
    <div class="card"><h3>Where the money goes</h3><table><tr><td>Editorial &amp; research</td><td><b>45%</b></td></tr><tr><td>Contest prizes &amp; community</td><td><b>20%</b></td></tr><tr><td>Hosting, tools, video production</td><td><b>15%</b></td></tr><tr><td>Marketing to reach people on day 1</td><td><b>15%</b></td></tr><tr><td>Operations</td><td><b>5%</b></td></tr></table><p class="small muted" style="margin-top:10px">Target allocation; published annually.</p></div>
    <div class="card"><h3>Other ways to support</h3><ul class="bullets"><li>Share a guide with someone who needs it</li><li><a href="{base}stories.html#submit">Submit your story</a></li><li>Whitelist ExLane in your ad blocker; ads are light by design</li><li>Use our <a href="{base}coaching.html">coach matching</a> if you need it (referral-funded)</li><li><a href="{base}careers.html">Volunteer</a> as a moderator, editor or translator</li></ul></div>
  </div>
  <p class="muted small center" style="margin-top:24px">ExLane is an independent publication, not a registered charity; support is a voluntary contribution, not a tax-deductible donation, unless stated otherwise for your region.</p>
</div></section>
"""})

# ------------------------------------------------------------------ CONTESTS
PAGES.append({"path": "contests.html", "title": "Contests & Prizes", "desc": "Monthly story contest, the 30-day glow-up challenge with prizes, and community awards. Free to enter.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Contests</span><h1>Contests &amp; prizes</h1><p class="lead">Recovery is easier with a deadline and a reason. Free to enter. Sponsored prizes; no purchase necessary.</p></div></section>
<section class="tight"><div class="wrap">{ad:leaderboard}</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="grid grid-3">
    <div class="card"><span class="tag tag-brand">Monthly</span><h3 style="margin-top:10px">Story of the Month</h3><p class="muted">Submit your recovery story. Readers vote; editors pick from the top five.</p><p><b>Prize:</b> $150 gift card + featured on the homepage and the channel.</p><a class="btn btn-primary" href="{base}stories.html#submit">Enter</a></div>
    <div class="card"><span class="tag tag-teal">Quarterly</span><h3 style="margin-top:10px">30-Day Glow-Up Challenge</h3><p class="muted">Complete all 30 days in the tool, then submit a before/after in your own words (no photos required).</p><p><b>Prize:</b> $300 towards a trip, course, or gym membership, sponsor-funded.</p><a class="btn btn-teal" href="#enter">Enter</a></div>
    <div class="card"><span class="tag tag-violet">Ongoing</span><h3 style="margin-top:10px">Lane-Keeper Awards</h3><p class="muted">Nominate a friend who showed up for you during your breakup. We send them a thank-you gift on your behalf.</p><p><b>Prize:</b> $50 gift + a printed note.</p><a class="btn btn-outline" href="#enter">Nominate</a></div>
  </div>
  <div class="lead-panel" id="enter" style="margin-top:34px">
    <div class="lead-split">
      <div><span class="eyebrow">Entry form</span><h2>Enter a contest</h2><p class="muted">One form for all contests. We reply to every entry.</p><h3>Rules in short</h3><ul class="bullets"><li>18+, one entry per person per contest per month</li><li>Original content only; we may edit for length and privacy</li><li>Winners announced on the first Monday of the month by email and on this page</li><li>Prizes delivered as gift cards or direct payment; no cash alternative unless stated</li><li>Void where prohibited; full <a href="{base}terms.html#contests">rules</a></li></ul></div>
      <form class="form" data-form="Contest entry"><input type="hidden" name="_gotcha">
        <div class="form-row"><div><label for="c-name">Name</label><input id="c-name" name="name" required></div><div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
        <div><label for="c-which">Contest</label><select id="c-which" name="contest"><option>Story of the Month</option><option>30-Day Glow-Up Challenge</option><option>Lane-Keeper Award (nomination)</option></select></div>
        <div><label for="c-country">Country</label><input id="c-country" name="country" required></div>
        <div><label for="c-entry">Your entry / nomination</label><textarea id="c-entry" name="entry" required></textarea></div>
        <label class="check"><input type="checkbox" name="rules" value="yes" required> I've read the rules and I'm 18 or older.</label>
        <label class="check"><input type="checkbox" name="newsletter" value="yes"> Also send me the weekly newsletter.</label>
        <button class="btn btn-grad" type="submit">Submit entry</button>
      </form>
      <div class="form-success">Entry received. Good luck; winners are announced on the first Monday of the month.</div>
    </div>
  </div>
  <div class="card" style="margin-top:26px"><h3>Sponsor a prize</h3><p class="muted">Brands that fit (wellness, travel, fitness, learning, self-care) can fund a prize and be named on this page and in the announcement email. <a href="{base}advertise.html#sponsor">Sponsorship details →</a></p></div>
</div></section>
"""})

# ------------------------------------------------------------------ CAREERS / TALENT
PAGES.append({"path": "careers.html", "title": "Careers, Coaches & Volunteers", "desc": "Work with ExLane: writers, video editors, community moderators, translators, breakup coaches and therapists. Remote, flexible, paid and volunteer roles.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Talent</span><h1>Work with ExLane</h1><p class="lead">Small team, remote, outcome-driven. We hire people who have been through it and people who can write, edit, moderate and coach with precision and warmth.</p></div></section>
<section style="padding-top:0"><div class="wrap">
  <h2>Open roles</h2>
  <div class="grid grid-2">
    <div class="card"><span class="tag tag-brand">Freelance · Paid</span><h3 style="margin-top:10px">Staff writer, recovery guides</h3><p class="muted">Long-form, research-backed guides (1,500–3,000 words). You cite studies, you cut fluff, you can write for someone crying at 2 a.m. without being saccharine. Per-piece rates.</p></div>
    <div class="card"><span class="tag tag-brand">Freelance · Paid</span><h3 style="margin-top:10px">Video editor / short-form producer</h3><p class="muted">Turn guides into 60–90 second explainers and 8–12 minute channel videos. Captions, pacing, thumbnails. Portfolio required.</p></div>
    <div class="card"><span class="tag tag-teal">Part-time · Paid</span><h3 style="margin-top:10px">Community &amp; stories editor</h3><p class="muted">Read submissions, reply kindly, edit for privacy and length, run the monthly contest, spot the story that will help the most people.</p></div>
    <div class="card"><span class="tag tag-violet">Volunteer</span><h3 style="margin-top:10px">Moderators &amp; translators</h3><p class="muted">Help keep the community safe and bring the guides into Spanish, Hindi, French, Portuguese, Tagalog and Arabic. Credit and references provided.</p></div>
  </div>
  <div class="card" id="coaches" style="margin-top:22px"><span class="tag tag-teal">Partners</span><h3 style="margin-top:10px">Breakup coaches &amp; licensed therapists</h3><p class="muted">Join the matching list. We check credentials, insurance and references, and we monitor client feedback. You set your rates and formats; we send matched leads and take a referral fee on bookings.</p></div>
  {ad:in-article}
  <div class="lead-panel" style="margin-top:30px">
    <div class="lead-split">
      <div><span class="eyebrow">Apply</span><h2>Tell us what you'd do here</h2><p class="muted">No CV formatting contests. Links and three honest sentences beat a cover letter.</p></div>
      <form class="form" data-form="Talent application"><input type="hidden" name="_gotcha">
        <div class="form-row"><div><label for="t-name">Name</label><input id="t-name" name="name" required></div><div><label for="t-email">Email</label><input id="t-email" type="email" name="email" required></div></div>
        <div class="form-row"><div><label for="t-role">Role</label><select id="t-role" name="role"><option>Staff writer</option><option>Video editor / producer</option><option>Community &amp; stories editor</option><option>Moderator (volunteer)</option><option>Translator (volunteer)</option><option>Breakup coach (partner)</option><option>Licensed therapist (partner)</option><option>Something else</option></select></div><div><label for="t-loc">Location &amp; time zone</label><input id="t-loc" name="location"></div></div>
        <div><label for="t-links">Links (portfolio, LinkedIn, samples, credentials)</label><input id="t-links" name="links" placeholder="One per line or comma-separated"></div>
        <div><label for="t-why">Why you, in three sentences</label><textarea id="t-why" name="pitch" required></textarea></div>
        <div><label for="t-rate">Rate expectation <span class="muted">(optional)</span></label><input id="t-rate" name="rate"></div>
        <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="{base}privacy.html">privacy policy</a>.</label>
        <button class="btn btn-grad" type="submit">Send application</button>
      </form>
      <div class="form-success">Received. We reply to every application within two weeks.</div>
    </div>
  </div>
</div></section>
"""})

# ------------------------------------------------------------------ ADVERTISE / SPONSOR / PARTNER
PAGES.append({"path": "advertise.html", "title": "Advertise, Sponsor & Partner", "desc": "Reach people at the moment they're rebuilding their lives: sponsorships, display and native placements, newsletter slots, contest prizes, creator features and referral partnerships with ExLane.", "body": """
<section class="page-head"><div class="wrap"><span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach people at the exact moment they're rebuilding</h1><p class="lead">Breakup recovery is a life-reset moment: new routines, new gym, new city, new apps, new therapy. ExLane meets people there with tools they use daily, not a page they skim once.</p></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="stats"><div class="stat"><b>Daily</b>tool users return 5–30 days in a row</div><div class="stat"><b>18–44</b>core audience, global English</div><div class="stat"><b>Intent</b>wellness, fitness, travel, learning, therapy, dating</div><div class="stat"><b>Light</b>ad load: fewer, better placements</div></div>
  <div class="divider"></div>
  <div class="grid grid-3">
    <div class="card" id="sponsor"><div class="ico">🏆</div><h3>Sponsor a contest or tool</h3><p class="muted">Name on the contest page, the announcement email, and the tool itself ("Glow-Up Challenge, supported by…"). From $250/month.</p></div>
    <div class="card"><div class="ico">📰</div><h3>Newsletter &amp; native</h3><p class="muted">One sponsor slot per weekly email and a clearly labelled native placement in the guides. Wellness, fitness, travel, learning and therapy brands only.</p></div>
    <div class="card"><div class="ico">📺</div><h3>Display placements</h3><p class="muted">Programmatic via Google AdSense plus a limited number of direct-sold leaderboard and sidebar units.</p></div>
    <div class="card" id="partners"><div class="ico">🤝</div><h3>Referral partnerships</h3><p class="muted">Therapy platforms, coaching networks, apps and courses: performance-based partnerships with transparent disclosure to readers.</p></div>
    <div class="card" id="creators"><div class="ico">🎥</div><h3>Creator features</h3><p class="muted">Coaches, therapists and creators whose videos match the evidence get featured on the videos page and in guides.</p></div>
    <div class="card"><div class="ico">🌐</div><h3>Domain &amp; site partnership</h3><p class="muted">Interested in the ExLane.com domain, the site, or a joint venture? Use the link at the very top of every page.</p></div>
  </div>
  <div class="callout" style="margin-top:26px"><b>What we don't run:</b> gambling, payday loans, "get your ex back" manipulation products, supplements with medical claims, or anything that preys on someone's worst week. If your product wouldn't pass that test, this isn't the right audience.</div>
  <div class="lead-panel" style="margin-top:30px">
    <div class="lead-split">
      <div><span class="eyebrow">Get the media kit</span><h2>Tell us what you're promoting</h2><p class="muted">We reply within two business days with rates, audience data and available dates.</p></div>
      <form class="form" data-form="Advertising / sponsorship inquiry"><input type="hidden" name="_gotcha">
        <div class="form-row"><div><label for="a-name">Name</label><input id="a-name" name="name" required></div><div><label for="a-email">Work email</label><input id="a-email" type="email" name="email" required></div></div>
        <div class="form-row"><div><label for="a-co">Company / brand</label><input id="a-co" name="company" required></div><div><label for="a-url">Website</label><input id="a-url" type="url" name="website" placeholder="https://"></div></div>
        <div><label>Interested in</label><div class="chips"><span class="chip">Contest / tool sponsorship</span><span class="chip">Newsletter slot</span><span class="chip">Native placement</span><span class="chip">Display ads</span><span class="chip">Referral partnership</span><span class="chip">Creator feature</span><span class="chip">Domain / site partnership</span></div><input type="hidden" name="interest" data-chips></div>
        <div class="form-row"><div><label for="a-budget">Monthly budget</label><select id="a-budget" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Performance-only</option></select></div><div><label for="a-when">Timing</label><input id="a-when" name="timing" placeholder="e.g. Q1 2027"></div></div>
        <div><label for="a-msg">Details</label><textarea id="a-msg" name="details"></textarea></div>
        <button class="btn btn-grad" type="submit">Request media kit</button>
      </form>
      <div class="form-success">Thanks. Expect the media kit within two business days.</div>
    </div>
  </div>
</div></section>
"""})

# ------------------------------------------------------------------ ABOUT
PAGES.append({"path": "about.html", "title": "About ExLane", "desc": "Why ExLane exists, how it's funded, and the editorial standards behind every guide.", "body": """
<section class="page-head"><div class="wrap-narrow"><span class="eyebrow">About</span><h1>Why ExLane exists</h1><p class="lead">Most breakup advice online is either a listicle written in an afternoon or a funnel for a "get them back" course. Neither helps at 2 a.m. on day 3. ExLane is the third option: tools you use in the moment, guides checked against research, and honest routes to a human when you need one.</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow article">
<h2>What we believe</h2>
<ul><li><strong>Heartbreak is a physical event.</strong> It responds to sleep, movement, no-contact and time, not to willpower or shame.</li><li><strong>Tools beat advice.</strong> A timer you press beats a paragraph you read.</li><li><strong>Nobody should have to sign up to feel better.</strong> Every tool works without an account and stores data only on your device.</li><li><strong>Honesty over engagement.</strong> We'll tell you to close the tab and call a friend when that's the right answer.</li></ul>
<h2>Editorial standards</h2>
<p>Guides are written against published relationship-psychology and neuroscience research and are reviewed for accuracy before publication. Where evidence is mixed (rebounds, for example), we say so. We do not publish "get your ex back" manipulation content. Sponsored and affiliate content is labelled. See the <a href="{base}disclaimer.html">disclaimers</a>.</p>
<h2>How ExLane is funded</h2>
<p>Light display advertising, clearly labelled referral partnerships (coaching and therapy platforms), sponsorships that pass our fit test, and reader support. That mix keeps the tools free. <a href="{base}donate.html">Support us</a> or <a href="{base}advertise.html">partner with us</a>.</p>
<h2>The name</h2>
<p>"Ex lane": the lane you take to get past an ex, fast. ExLane is an independent publication and is not affiliated with any similarly named company, product or mark. <a href="{base}disclaimer.html">Trademark notice</a>.</p>
<h2>Contact</h2>
<p>Editorial, corrections, press, partnerships, or interest in the site or domain: <a href="{base}contact.html">contact page</a>.</p>
</div></section>
"""})

# ------------------------------------------------------------------ CONTACT
PAGES.append({"path": "contact.html", "title": "Contact ExLane", "desc": "Contact ExLane for editorial, corrections, partnerships, sponsorship, advertising, press, or interest in the website or domain.", "body": """
<section class="page-head"><div class="wrap-narrow"><span class="eyebrow">Contact</span><h1>Get in touch</h1><p class="lead">One inbox, read by a human. For coaching requests use the <a href="{base}coaching.html">matching form</a>; for stories use the <a href="{base}stories.html#submit">story form</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow">
  <div class="grid grid-2" style="margin-bottom:26px">
    <div class="card"><h3>Website, domain, sponsorship, advertising or partnership</h3><p class="muted">Use the dedicated link at the top of every page.</p><a class="btn btn-primary" href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact →</a></div>
    <div class="card"><h3>Everything else</h3><p class="muted">Corrections, press, feedback, accessibility issues, privacy requests.</p><a class="btn btn-outline" href="#" data-contact data-subject="ExLane contact">Email us</a></div>
  </div>
  <div class="lead-panel">
    <form class="form" data-form="Contact form"><input type="hidden" name="_gotcha">
      <div class="form-row"><div><label for="k-name">Name</label><input id="k-name" name="name" required></div><div><label for="k-email">Email</label><input id="k-email" type="email" name="email" required></div></div>
      <div><label for="k-topic">Topic</label><select id="k-topic" name="topic"><option>General</option><option>Correction to a guide</option><option>Press / media</option><option>Privacy request</option><option>Accessibility issue</option><option>Report a problem with a coach</option><option>Website / domain / sponsorship / advertising / partnership</option></select></div>
      <div><label for="k-msg">Message</label><textarea id="k-msg" name="message" required></textarea></div>
      <button class="btn btn-grad" type="submit">Send message</button>
      <p class="form-note">We aim to reply within three business days. If you're in crisis, please use the resources in the footer instead.</p>
    </form>
    <div class="form-success">Message sent. Thank you.</div>
  </div>
</div></section>
"""})

# ------------------------------------------------------------------ LEGAL
PAGES.append({"path": "privacy.html", "title": "Privacy Policy", "desc": "How ExLane handles data: tools store data only on your device; forms are sent by email; advertising and analytics cookies are disclosed here.", "body": """
<section class="page-head"><div class="wrap-narrow"><span class="eyebrow">Legal</span><h1>Privacy policy</h1><p class="muted">Effective 26 September 2026</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow article">
<h2>1. The short version</h2><p>The interactive tools (tracker, SOS, challenge, journal, reasons list, letter, quiz) store data <strong>only in your browser's local storage</strong>. Nothing you type into a tool is sent to us. Forms you submit (coaching, stories, contests, applications, newsletter, contact) are delivered to our inbox by email and used only for the purpose you submitted them for.</p>
<h2>2. Data we receive</h2><ul><li><strong>Form submissions:</strong> the fields you fill in, your email address, and the page you submitted from.</li><li><strong>Analytics:</strong> if enabled, aggregated page-view data (Google Analytics or a privacy-preserving equivalent). No tool contents are ever included.</li><li><strong>Advertising:</strong> Google AdSense may set cookies and use identifiers to serve and measure ads, including personalised ads where permitted. You can opt out at <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a> and at <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites.</li><li><strong>Embedded video:</strong> YouTube videos load only after you press play and use the privacy-enhanced (youtube-nocookie) domain.</li></ul>
<h2>3. How we use it</h2><p>To respond to you, match you with coaches you asked to be matched with, publish stories you asked us to publish, run contests you entered, send newsletters you subscribed to, and improve the site. We do not sell personal data.</p>
<h2>4. Sharing</h2><p>Coaching requests are shared with the coaches you are matched with. Referral partners receive only what's needed to attribute a referral (typically a click, not your details). Service providers (email, hosting, analytics, ads) process data under their own policies.</p>
<h2>5. Retention and your rights</h2><p>Form data is retained as long as needed for its purpose and deleted on request. You can request access, correction or deletion via the <a href="{base}contact.html">contact page</a> (topic: privacy request). Local-storage data is under your control: use "erase it all" on the tools page or clear your browser storage.</p>
<h2>6. Children</h2><p>ExLane is for adults. We do not knowingly collect data from anyone under 18.</p>
<h2>7. International</h2><p>The site is hosted on infrastructure that may be located outside your country. By using it you accept that transfer. EU/UK residents have rights under GDPR/UK GDPR; California residents have rights under the CCPA; both can be exercised through the contact page.</p>
<h2>8. Changes</h2><p>We'll post changes here with a new effective date.</p>
</div></section>
"""})

PAGES.append({"path": "terms.html", "title": "Terms of Use", "desc": "Terms of use for ExLane.com, including content licence for submitted stories and contest rules.", "body": """
<section class="page-head"><div class="wrap-narrow"><span class="eyebrow">Legal</span><h1>Terms of use</h1><p class="muted">Effective 26 September 2026</p></div></section>
<section style="padding-top:0"><div class="wrap-narrow article">
<h2>1. Acceptance</h2><p>By using ExLane.com you agree to these terms and the <a href="{base}privacy.html">privacy policy</a>. If you don't agree, don't use the site.</p>
<h2>2. Not professional advice</h2><p>Content and tools are for general information and self-reflection only. They are not medical, psychological, legal or financial advice and do not create a clinician–patient relationship. If you are in crisis, contact emergency services or a crisis line. See the <a href="{base}disclaimer.html">disclaimers</a>.</p>
<h2>3. Coaching referrals</h2><p>Coaches and therapists we refer you to are independent. ExLane does not provide coaching or therapy and is not responsible for their services. We may receive a referral fee.</p>
<h2>4. Your submissions</h2><p>By submitting a story, contest entry, comment or video, you confirm it is your own, you are 18 or older, and you grant ExLane a worldwide, royalty-free, perpetual licence to publish, edit, excerpt, translate and adapt it in any medium, with or without attribution as you specify. You can ask us to remove a published story at any time and we will, within a reasonable period.</p>
<h2 id="contests">5. Contest rules</h2><p>Open to residents aged 18+ where legal. No purchase necessary. One entry per person per contest per period. Entries judged on relevance, honesty, craft and helpfulness to other readers; reader votes may inform shortlists. Winners notified by email; unclaimed prizes after 30 days may be reassigned. Prizes are non-transferable and have no cash alternative unless stated. Sponsors do not judge. Void where prohibited. ExLane may cancel or modify a contest for reasons beyond its control.</p>
<h2>6. Acceptable use</h2><p>Don't post others' private information, harass anyone (including an ex), scrape the site, or use it for anything unlawful.</p>
<h2>7. Intellectual property</h2><p>Site content is © ExLane.com unless stated. Guides may be quoted with attribution and a link. Embedded videos belong to their creators.</p>
<h2>8. Liability</h2><p>The site is provided "as is". To the fullest extent permitted by law, ExLane is not liable for any loss arising from use of the site, its tools, or referred services.</p>
<h2>9. Changes and law</h2><p>We may update these terms; continued use means acceptance. Governing law: the jurisdiction of the operator, unless your local consumer law provides otherwise.</p>
</div></section>
"""})

PAGES.append({"path": "disclaimer.html", "title": "Disclaimers & Trademark Notice", "desc": "ExLane's medical, advertising, affiliate, and trademark/copyright disclosures.", "body": """
<section class="page-head"><div class="wrap-narrow"><span class="eyebrow">Legal</span><h1>Disclaimers &amp; trademark notice</h1></div></section>
<section style="padding-top:0"><div class="wrap-narrow article">
<h2>Trademark and copyright notice</h2>
<p>"ExLane" and "ExLane.com" are used here as the name of an independent online publication about breakup recovery, operated under the domain name exlane.com. ExLane.com is <strong>not affiliated with, endorsed by, sponsored by, or connected to</strong> any other company, product, service or trademark that uses "Exlane", "Ex Lane", "Everlane", "Express Lane", "Expresslane", "Exlan", "OpenLane" or any similar name, in any industry, anywhere in the world. Any such names, logos and marks belong to their respective owners. No claim is made to any registered trademark held by a third party, and nothing on this site should be read as an assertion of rights over such marks.</p>
<p>The ExLane.com name, logo, site design, guides, tools and original text are © ExLane.com. Embedded videos, quoted studies and referenced publications remain the property of their respective owners and are used under fair use / fair dealing for commentary and education, or under the platforms' embedding terms.</p>
<p>If you believe content on this site infringes your trademark or copyright, contact us via the <a href="{base}contact.html">contact page</a> with the details and we will respond promptly.</p>
<h2>Not medical or professional advice</h2>
<p>ExLane provides general information and self-help tools. Nothing here is a diagnosis, treatment, or a substitute for care from a licensed physician, psychologist, therapist, lawyer or financial adviser. If you have thoughts of harming yourself or others, contact emergency services or a crisis line immediately.</p>
<h2>Advertising and affiliate disclosure</h2>
<p>ExLane displays advertising (including Google AdSense) and participates in referral and affiliate programmes with coaching, therapy, app and course providers. When you click a partner link or book through our matching form, we may earn a fee at no extra cost to you. Sponsored placements are labelled. Advertising does not influence what the guides say.</p>
<h2>Video and third-party content</h2>
<p>Videos on this site are embedded from YouTube under YouTube's terms of service and remain the property of their creators. Featuring a video is not an endorsement of every claim in it.</p>
<h2>Stories</h2>
<p>Reader stories are personal accounts, lightly edited, with names changed on request. They describe what worked for one person and are not recommendations.</p>
</div></section>
"""})

PAGES.append({"path": "404.html", "title": "Page not found", "desc": "That page took a different lane.", "body": """
<section class="hero"><div class="lane-bg"></div><div class="wrap-narrow center"><span class="eyebrow">404</span><h1>That page took a different lane</h1><p class="lead">It moved, or never existed. Here's where to go instead.</p><div class="hero-cta" style="justify-content:center"><a class="btn btn-grad" href="index.html">Home</a><a class="btn btn-outline" href="quiz.html">Take the quiz</a><a class="btn btn-outline" href="tools.html">Open the tools</a></div></div></section>
"""})
