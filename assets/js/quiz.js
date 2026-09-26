/* ExLane.com — "Are You Really Over Your Ex?" scored quiz → lead capture */
(function () {
  "use strict";
  var qs = [
    { q: "How often do you check their social media (including 'accidentally')?", a: [["Never — muted, blocked, or just don't", 0], ["Once a week or less", 1], ["A few times a week", 2], ["Daily or more", 3]] },
    { q: "When you hear their name, what happens in your body?", a: [["Nothing much", 0], ["A small twinge", 1], ["A noticeable drop or spike", 2], ["Full stomach flip / heat / tears", 3]] },
    { q: "Are you currently in contact with them?", a: [["No, and I don't want to be", 0], ["No, but I think about reaching out", 1], ["Occasionally (birthdays, 'just checking in')", 2], ["Regularly / we still text or hook up", 3]] },
    { q: "How long since the breakup?", a: [["More than a year", 0], ["6–12 months", 1], ["1–6 months", 2], ["Less than a month", 3]] },
    { q: "When you imagine them happy with someone new:", a: [["Good for them, honestly", 0], ["Slight sting, then fine", 1], ["It bothers me for a day", 2], ["I can't think about it", 3]] },
    { q: "Do you still have their things, photos, or shared accounts active?", a: [["All cleared", 0], ["Mostly cleared", 1], ["A few things I 'haven't got around to'", 2], ["Everything's still there", 3]] },
    { q: "Who do you compare new people to?", a: [["Nobody — I take people as they are", 0], ["Rarely them", 1], ["Often them", 2], ["Everyone loses to them", 3]] },
    { q: "How are your sleep, appetite, and focus right now?", a: [["Normal", 0], ["Slightly off", 1], ["Noticeably worse", 2], ["Wrecked", 3]] },
    { q: "If they asked to get back together tomorrow:", a: [["Clear no", 0], ["Probably no", 1], ["I'd want to talk about it", 2], ["Yes, immediately", 3]] },
    { q: "What are you doing with the time you used to spend on them?", a: [["New routines, people, projects", 0], ["Some new things", 1], ["Mostly the same, minus them", 2], ["Waiting / replaying", 3]] }
  ];
  var bands = [
    { max: 6, title: "Green light: you're through it", tag: "tag-teal", body: "Your score says the attachment has dissolved and your life has refilled the space. What's left is maintenance: keep the boundaries that got you here and notice if you ever start reopening old doors 'just to check'.", cta: "Get the Dating Again Checklist", stage: "Ready" },
    { max: 13, title: "Yellow: mostly over it, a few loose wires", tag: "tag-violet", body: "You've done most of the work. The remaining pull is habit, not love — usually social media checks, leftover objects, or one unanswered question. Cut the last threads and the rest fades on its own within a few weeks.", cta: "Get the 14-Day Loose-Ends Plan", stage: "Loose ends" },
    { max: 21, title: "Amber: still in the recovery lane", tag: "tag-brand", body: "You're grieving, which is appropriate, but the contact and comparison patterns are keeping the wound open. The single highest-leverage move is a full 30-day no-contact block with the tracker, plus one replacement routine per week.", cta: "Start the 30-Day No-Contact Plan", stage: "Recovering" },
    { max: 99, title: "Red: you're not over them — yet", tag: "tag-brand", body: "Ongoing contact plus a strong body response plus nothing new filling the space equals a breakup that hasn't actually happened emotionally. That's fixable, but not by waiting. It needs structure: no-contact, a daily plan, and probably someone to talk to.", cta: "Talk to a breakup coach (free first call)", stage: "Acute" }
  ];
  var i = 0, score = 0, wrap = document.getElementById("quiz"); if (!wrap) return;
  var qEl = document.getElementById("quiz-q"), optEl = document.getElementById("quiz-opts"), bar = document.getElementById("quiz-bar"), cnt = document.getElementById("quiz-count");
  function render() {
    if (i >= qs.length) return finish();
    qEl.textContent = qs[i].q; cnt.textContent = "Question " + (i + 1) + " of " + qs.length; bar.style.width = (i / qs.length * 100) + "%"; optEl.innerHTML = "";
    qs[i].a.forEach(function (o) { var b = document.createElement("button"); b.type = "button"; b.textContent = o[0]; b.addEventListener("click", function () { score += o[1]; i++; render(); }); optEl.appendChild(b); });
  }
  function finish() {
    bar.style.width = "100%"; cnt.textContent = "Complete";
    var band = bands.filter(function (b) { return score <= b.max; })[0];
    document.getElementById("quiz-body").hidden = true;
    var r = document.getElementById("quiz-result"); r.classList.add("show");
    document.getElementById("res-score").textContent = score + " / 30";
    var t = document.getElementById("res-title"); t.textContent = band.title;
    document.getElementById("res-tag").className = "tag " + band.tag; document.getElementById("res-tag").textContent = band.stage;
    document.getElementById("res-body").textContent = band.body;
    document.getElementById("res-cta").textContent = band.cta;
    var st = document.getElementById("res-stage"); if (st) st.value = band.stage + " (" + score + "/30)";
    try { localStorage.setItem("exlane-quiz", JSON.stringify({ score: score, stage: band.stage, at: Date.now() })); } catch (e) {}
  }
  document.getElementById("quiz-restart").addEventListener("click", function () { i = 0; score = 0; document.getElementById("quiz-body").hidden = false; document.getElementById("quiz-result").classList.remove("show"); render(); });
  render();
})();
