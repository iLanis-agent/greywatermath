# Greywater math

Laundry-to-landscape greywater planning arithmetic: the loads name the liters, the liters name the basins, and the run names the pipe.

Live at https://ilanis-agent.github.io/greywatermath/

## The three tools

- **Flow plan** - liters = loads x labeled 110 L per load, with a daily average and watering-can, hose-day and coin-op bands.
- **Basin plan** - basins = ceil(weekly liters / labeled 40 L per mulch basin), with balcony, backyard and orchard bands.
- **Pipe plan** - drop = run x labeled 2 cm fall per meter; sticks = ceil(run / labeled 3 m), with short-run, across-the-yard and long-pull bands.

## Formulas and limits

- Volumes and drops are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: liters per load, basin volume, fall per meter, stick length.
- Illustrative planning arithmetic only. Real systems follow local plumbing and health rules: never store greywater, no sprays, subsurface mulch basins only. This is not a permit.

## Development

- `engine.js` - calculation and render engine (browser global `GreywaterMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
