/* ExLane.com — interactive recovery tools (localStorage only; nothing leaves the browser) */
(function () {
  "use strict";
  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function get(k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  var DAY = 864e5;

  /* ---------- 1. No-Contact Day Counter ---------- */
  (function () {
    var box = $("#nc-tool"); if (!box) return;
    var input = $("#nc-date"), out = $("#nc-days"), ring = $("#nc-ring"), ringTxt = $("#nc-ring-text"), msg = $("#nc-msg"), goalSel = $("#nc-goal");
    var state = get("exlane-nc", { start: null, goal: 30, relapses: [] });
    if (state.start) input.value = state.start; goalSel.value = String(state.goal);
    var messages = [
      [0, "Day 0. The hardest decision is already made. Everything from here is momentum."],
      [3, "Days 1–3 are chemical withdrawal. Cravings peak here, then fall. Ride it out."],
      [7, "One week. The urge to check their profile is a habit loop now, not love. Break the loop."],
      [14, "Two weeks. Most people report the first genuinely okay day around here."],
      [21, "Three weeks. New routines are forming. Protect them."],
      [30, "30 days. You have proven you can live without contact. Extend the goal or start the Glow-Up Plan."],
      [60, "60 days. You are no longer recovering. You are rebuilding."],
      [90, "90 days. Statistically the point where most people are ready to date again on their own terms."]
    ];
    function render() {
      if (!state.start) { out.textContent = "—"; ringTxt.textContent = "0%"; ring.style.setProperty("--p", 0); msg.textContent = "Pick the date you went no-contact to start the counter."; return; }
      var days = Math.max(0, Math.floor((Date.now() - new Date(state.start + "T00:00:00").getTime()) / DAY));
      out.textContent = days;
      var pct = Math.min(100, Math.round(days / state.goal * 100));
      ring.style.setProperty("--p", pct); ringTxt.textContent = pct + "%";
      var m = messages[0][1]; messages.forEach(function (x) { if (days >= x[0]) m = x[1]; }); msg.textContent = m;
      $("#nc-relapses").textContent = state.relapses.length;
    }
    input.addEventListener("change", function () { state.start = input.value || null; set("exlane-nc", state); render(); });
    goalSel.addEventListener("change", function () { state.goal = Number(goalSel.value); set("exlane-nc", state); render(); });
    $("#nc-reset").addEventListener("click", function () { if (!confirm("Reset the counter to today? Your previous streak will be logged as a relapse.")) return; if (state.start) state.relapses.push(state.start); state.start = new Date().toISOString().slice(0, 10); input.value = state.start; set("exlane-nc", state); render(); });
    render();
  })();

  /* ---------- 2. Urge SOS (10-minute delay + grounding) ---------- */
  (function () {
    var btn = $("#sos-start"); if (!btn) return;
    var timerEl = $("#sos-timer"), stepEl = $("#sos-step"), t = null, left = 600;
    var steps = [
      "Put the phone face-down. You are not deciding anything for 10 minutes.",
      "Name 5 things you can see. 4 you can touch. 3 you can hear. 2 you can smell. 1 you can taste.",
      "Write the text you want to send in the journal box below instead. Do not send it.",
      "Ask: what do I actually want from contact? Relief, not them. Relief is available elsewhere.",
      "Drink a glass of water. Walk to a different room. Change the physical state.",
      "Read your own 'why I left' note (Tools → Reasons List).",
      "Message someone who supports you. Say: 'having an urge, talk to me about anything for 5 minutes.'",
      "The urge peaks and passes like a wave. Notice it falling.",
      "Decide: was the urge about them, or about being alone right now?",
      "Timer done. If you still want to text, wait until tomorrow morning and re-read this."
    ];
    function tick() { left--; var m = Math.floor(left / 60), s = left % 60; timerEl.textContent = m + ":" + (s < 10 ? "0" : "") + s; stepEl.textContent = steps[Math.min(9, Math.floor((600 - left) / 60))]; if (left <= 0) { clearInterval(t); btn.textContent = "Start another 10 minutes"; btn.disabled = false; var log = get("exlane-sos", 0) + 1; set("exlane-sos", log); $("#sos-count").textContent = log; } }
    btn.addEventListener("click", function () { left = 600; clearInterval(t); t = setInterval(tick, 1000); btn.disabled = true; btn.textContent = "Running…"; stepEl.textContent = steps[0]; });
    $("#sos-count").textContent = get("exlane-sos", 0);
  })();

  /* ---------- 3. 30-Day Glow-Up Challenge ---------- */
  (function () {
    var cal = $("#glow-cal"); if (!cal) return;
    var tasks = ["Delete or archive their photos from your phone.", "Mute/unfollow their accounts. Do not block-unblock cycle.", "Do 20 minutes of any movement you enjoy.", "Write 3 reasons the relationship ended (your honest version).", "Sleep 8 hours. Phone outside the bedroom.", "Reconnect with one friend you neglected.", "Clean and rearrange one room.", "Cook one real meal for yourself.", "List 10 things you stopped doing during the relationship. Do one.", "Try a new coffee shop, park, or route.", "Write a letter to them you will never send. Burn or delete it.", "Book one appointment you've been avoiding (dentist, haircut, doctor).", "Spend 1 hour phone-free outdoors.", "Learn something for 30 minutes (language app, tutorial, book).", "Halfway. Re-read day 4. Notice what changed.", "Do something that scares you slightly.", "Buy or make one thing that upgrades your daily life.", "No sad playlists today. Build a forward playlist.", "Say no to one thing you don't want to do.", "Write down 3 non-negotiables for your next relationship.", "Volunteer, donate, or help someone anonymously.", "Photograph something beautiful. Post it or keep it.", "Plan a trip, even a day trip. Put a date on it.", "Talk to one new person (in real life).", "Review your finances for 30 minutes. Cancel one leech subscription.", "Do a hard workout or a long walk.", "Write the story of the breakup in the third person. Notice the plot.", "Tell someone what you're proud of this month.", "Reset your bedroom, desk, or wardrobe for the next chapter.", "Day 30: write a note to Day-1 you. Then decide your next 30."];
    var done = get("exlane-glow", {});
    var startKey = "exlane-glow-start"; var start = get(startKey, null); if (!start) { start = new Date().toISOString().slice(0, 10); set(startKey, start); }
    var todayIdx = Math.floor((Date.now() - new Date(start + "T00:00:00").getTime()) / DAY);
    for (var i = 0; i < 30; i++) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = i + 1; b.setAttribute("aria-label", "Day " + (i + 1) + ": " + tasks[i]); b.title = tasks[i];
      if (done[i]) b.classList.add("done"); if (i === todayIdx) b.classList.add("today");
      (function (i, b) { b.addEventListener("click", function () { $("#glow-task").textContent = "Day " + (i + 1) + ": " + tasks[i]; $("#glow-toggle").dataset.day = i; $("#glow-toggle").textContent = done[i] ? "Mark day " + (i + 1) + " not done" : "Mark day " + (i + 1) + " done"; }); })(i, b);
      cal.appendChild(b);
    }
    function refresh() { var n = Object.keys(done).filter(function (k) { return done[k]; }).length; $("#glow-progress").style.width = (n / 30 * 100) + "%"; $("#glow-count").textContent = n; $all("button", cal).forEach(function (b, i) { b.classList.toggle("done", !!done[i]); }); }
    $("#glow-toggle").addEventListener("click", function () { var i = Number(this.dataset.day); if (isNaN(i)) return; done[i] = !done[i]; set("exlane-glow", done); this.textContent = done[i] ? "Mark day " + (i + 1) + " not done" : "Mark day " + (i + 1) + " done"; refresh(); });
    $("#glow-task").textContent = "Today: Day " + Math.min(30, Math.max(1, todayIdx + 1)) + " — " + tasks[Math.min(29, Math.max(0, todayIdx))];
    $("#glow-toggle").dataset.day = Math.min(29, Math.max(0, todayIdx));
    refresh();
  })();

  /* ---------- 4. Journal prompts + private journal ---------- */
  (function () {
    var p = $("#journal-prompt"); if (!p) return;
    var prompts = ["What did I need from this relationship that I can give myself this week?", "Write the text you want to send. Then write what you'd tell a friend who wanted to send it.", "What is one thing I'm relieved I no longer have to deal with?", "Describe today's grief like weather. What's the forecast for tomorrow?", "What did I learn about my boundaries?", "What did I stop doing while I was with them? Which one do I miss most?", "If the breakup were a door, what's the room on the other side?", "List three green flags I'll look for next time.", "What would 'over it' look like on an ordinary Tuesday?", "Who showed up for me this month? Thank one of them today."];
    var idx = get("exlane-prompt", Math.floor(Math.random() * prompts.length));
    function show() { p.textContent = prompts[idx % prompts.length]; }
    $("#journal-next").addEventListener("click", function () { idx++; set("exlane-prompt", idx); show(); });
    var ta = $("#journal-text"), entries = get("exlane-journal", []);
    $("#journal-save").addEventListener("click", function () { if (!ta.value.trim()) return; entries.unshift({ d: new Date().toISOString().slice(0, 10), p: prompts[idx % prompts.length], t: ta.value.trim() }); set("exlane-journal", entries); ta.value = ""; list(); });
    $("#journal-clear").addEventListener("click", function () { if (confirm("Delete all journal entries stored in this browser?")) { entries = []; set("exlane-journal", entries); list(); } });
    function list() { var ul = $("#journal-list"); ul.innerHTML = ""; $("#journal-n").textContent = entries.length; entries.slice(0, 10).forEach(function (e) { var li = document.createElement("li"); li.innerHTML = "<b>" + e.d + "</b> · <i class='muted'>" + e.p + "</i><br>" + e.t.replace(/</g, "&lt;"); ul.appendChild(li); }); }
    show(); list();
  })();

  /* ---------- 5. Reasons list (why I left / why it ended) ---------- */
  (function () {
    var form = $("#reasons-form"); if (!form) return;
    var items = get("exlane-reasons", []), ul = $("#reasons-list"), inp = $("#reason-input");
    function render() { ul.innerHTML = ""; items.forEach(function (r, i) { var li = document.createElement("li"); li.textContent = r + " "; var x = document.createElement("button"); x.type = "button"; x.className = "btn btn-sm btn-ghost"; x.textContent = "remove"; x.addEventListener("click", function () { items.splice(i, 1); set("exlane-reasons", items); render(); }); li.appendChild(x); ul.appendChild(li); }); }
    form.addEventListener("submit", function (e) { e.preventDefault(); if (!inp.value.trim()) return; items.push(inp.value.trim()); set("exlane-reasons", items); inp.value = ""; render(); });
    render();
  })();

  /* ---------- 6. Closure letter generator ---------- */
  (function () {
    var f = $("#letter-form"); if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var n = f.name.value || "you", g = f.grateful.value, h = f.hurt.value, l = f.lesson.value, fut = f.future.value;
      var txt = "Dear " + n + ",\n\nI'm writing this for me, not for you, and you will never read it.\n\nI'm grateful for " + (g || "the good parts, and there were some") + ".\n\nWhat hurt was " + (h || "how it ended") + ". I'm allowed to be angry about that, and I'm allowed to put it down.\n\nWhat I learned: " + (l || "what I need and what I won't accept again") + ".\n\nWhere I'm going: " + (fut || "forward, in my own lane") + ".\n\nI'm not waiting for an apology. I'm closing this myself.\n\n— Me";
      $("#letter-out").value = txt; $("#letter-out").scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
    $("#letter-copy").addEventListener("click", function () { navigator.clipboard && navigator.clipboard.writeText($("#letter-out").value); this.textContent = "Copied"; });
  })();

  /* ---------- 7. Export / erase all local data ---------- */
  var erase = $("#erase-all"); if (erase) erase.addEventListener("click", function () { if (!confirm("Erase every ExLane tool record stored in this browser?")) return; Object.keys(localStorage).forEach(function (k) { if (k.indexOf("exlane-") === 0) localStorage.removeItem(k); }); location.reload(); });
})();
