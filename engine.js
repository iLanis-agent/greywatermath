(function (root) {
  "use strict";
  var LOAD_L = 110;   // labeled liters per top-loader wash load
  var BASIN_L = 40;   // labeled mulch-basin volume, L
  var FALL_CM = 2;    // labeled pipe fall per meter, cm/m
  var STICK_M = 3;    // labeled pipe stick length, m

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function flowPlan(loads) {
    if (!(loads > 0)) return { error: "the weekly loads must be positive" };
    var liters = round1(loads * LOAD_L);
    var daily = round1(liters / 7);
    var verdict;
    if (liters <= 220) verdict = "a watering-can week";
    else if (liters <= 770) verdict = "a hose-day week";
    else verdict = "a coin-op week";
    return { liters: liters, daily: daily, verdict: verdict };
  }

  function basinPlan(liters) {
    if (!(liters > 0)) return { error: "the weekly liters must be positive" };
    var basins = Math.ceil(liters / BASIN_L);
    var verdict;
    if (basins <= 5) verdict = "a balcony run";
    else if (basins <= 20) verdict = "a backyard run";
    else verdict = "an orchard run";
    return { basins: basins, verdict: verdict };
  }

  function pipePlan(distM) {
    if (!(distM > 0)) return { error: "the run length must be positive" };
    var drop = round1(distM * FALL_CM);
    var sticks = Math.ceil(distM / STICK_M);
    var verdict;
    if (distM <= 5) verdict = "a short run";
    else if (distM <= 20) verdict = "across the yard";
    else verdict = "a long pull";
    return { drop: drop, sticks: sticks, verdict: verdict };
  }

  function renderFlow(r, loads) {
    return plural(loads, "load") + " a week at a labeled " + LOAD_L + " L per load sends " + r.liters
      + " L to the garden - " + r.daily + " L a day, " + r.verdict + ".";
  }

  function renderBasin(r, liters) {
    return liters + " L a week fills " + plural(r.basins, "mulch basin") + " of a labeled " + BASIN_L
      + " L - " + r.verdict + ".";
  }

  function renderPipe(r, distM) {
    return "A run of " + distM + " m at a labeled " + FALL_CM + " cm fall per meter drops " + r.drop
      + " cm and takes " + plural(r.sticks, "stick") + " of labeled " + STICK_M + " m pipe - " + r.verdict + ".";
  }

  var api = { flowPlan: flowPlan, basinPlan: basinPlan, pipePlan: pipePlan, renderFlow: renderFlow, renderBasin: renderBasin, renderPipe: renderPipe };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.GreywaterMath = api;
})(this);
