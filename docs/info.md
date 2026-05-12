## How it works

This project implements a 4-bit synchronous up counter using Verilog HDL.  
The counter increments its value by 1 on every positive edge of the clock signal.

The design uses:
- `clk` as the clock input
- `rst_n` as an active-low reset signal

When `rst_n` is low, the counter resets to `0000`.  
When reset is released, the counter counts upward continuously:

0000 → 0001 → 0010 → ... → 1111 → 0000

The 4-bit counter value is connected to:
- `uo_out[3:0]`

Unused output pins remain at logic `0`.

---

## How to test

1. Apply a clock signal to the design.
2. Keep `rst_n = 0` to reset the counter.
3. Change `rst_n = 1` to start counting.
4. Observe outputs:
   - `uo_out[0]` → Counter bit 0
   - `uo_out[1]` → Counter bit 1
   - `uo_out[2]` → Counter bit 2
   - `uo_out[3]` → Counter bit 3

The output value increases by 1 on every clock cycle.

Example sequence:

| Clock Cycle | Output |
|-------------|--------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| ... | ... |
| 15 | 1111 |

---

## External hardware

No external hardware is required.

Optional:
- LEDs can be connected to `uo_out[3:0]` to visualize the counter output.
