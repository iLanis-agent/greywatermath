import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

LOAD_L = 110
BASIN_L = 40
FALL_CM = 2
STICK_M = 3

def flow_plan(loads):
    if not (loads > 0):
        return {"error": "the weekly loads must be positive"}
    liters = round1(loads * LOAD_L)
    daily = round1(liters / 7)
    if liters <= 220: verdict = "a watering-can week"
    elif liters <= 770: verdict = "a hose-day week"
    else: verdict = "a coin-op week"
    return {"liters": liters, "daily": daily, "verdict": verdict}

def basin_plan(liters):
    if not (liters > 0):
        return {"error": "the weekly liters must be positive"}
    basins = math.ceil(liters / BASIN_L)
    if basins <= 5: verdict = "a balcony run"
    elif basins <= 20: verdict = "a backyard run"
    else: verdict = "an orchard run"
    return {"basins": basins, "verdict": verdict}

def pipe_plan(distM):
    if not (distM > 0):
        return {"error": "the run length must be positive"}
    drop = round1(distM * FALL_CM)
    sticks = math.ceil(distM / STICK_M)
    if distM <= 5: verdict = "a short run"
    elif distM <= 20: verdict = "across the yard"
    else: verdict = "a long pull"
    return {"drop": drop, "sticks": sticks, "verdict": verdict}

def render_flow(r, loads):
    return (plural(loads, "load") + " a week at a labeled " + fmt(LOAD_L) + " L per load sends " + fmt(r["liters"])
            + " L to the garden - " + fmt(r["daily"]) + " L a day, " + r["verdict"] + ".")

def render_basin(r, liters):
    return (fmt(liters) + " L a week fills " + plural(r["basins"], "mulch basin") + " of a labeled " + fmt(BASIN_L)
            + " L - " + r["verdict"] + ".")

def render_pipe(r, distM):
    return ("A run of " + fmt(distM) + " m at a labeled " + fmt(FALL_CM) + " cm fall per meter drops " + fmt(r["drop"])
            + " cm and takes " + plural(r["sticks"], "stick") + " of labeled " + fmt(STICK_M) + " m pipe - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[7],[2],[15],[1],[4],[10],[20],[3],[0],[6]]:
    add("flowPlan", flow_plan, render_flow, a)
for a in [[770],[100],[1000],[200],[40],[41],[220],[660],[0],[1500]]:
    add("basinPlan", basin_plan, render_basin, a)
for a in [[12],[4],[30],[1],[7],[25],[3.5],[18],[0],[50]]:
    add("pipePlan", pipe_plan, render_pipe, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
