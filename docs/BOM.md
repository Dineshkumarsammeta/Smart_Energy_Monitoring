# Bill of Materials (BOM) — Smart Energy Monitoring (Placeholder)

> **Safety note:** Documented for **low‑voltage DC** prototyping. Do **not** connect directly to mains AC without proper isolation and a qualified electrician. Use CT sensors designed for safe measurement.

| # | Component                              | Example Part (or spec)        | Qty | Notes |
|---|----------------------------------------|-------------------------------|-----|------|
| 1 | Microcontroller                         | Arduino UNO R3                | 1   | 5V logic |
| 2 | Current Transformer (CT)                | SCT‑013‑000 (100 A / 50 mA)   | 1   | Non‑invasive CT |
| 3 | ADC / Burden                            | ADS1115 16‑bit ADC            | 1   | Scaling & calibration |
| 4 | RS‑485 Transceiver                      | MAX485 module                 | 1   | DE/RE ↔ UNO pins |
| 5 | Relay Module (opto‑isolated)            | 1‑channel 5V relay            | 1   | D7 control |
| 6 | Indicator LED + Resistor                | 5mm LED + 220 Ω               | 1   | Status |
| 7 | DC Power Supply                         | 5V @ 2A                       | 1   | For UNO + modules |
| 8 | Terminal Blocks / Dupont Wires          | Assorted                      | —   | Safe connections |
| 9 | Breadboard / Proto PCB                  | Any                           | 1   | Prototyping |
|10 | Enclosure (optional)                    | ABS box                       | 1   | Safety |

**Calibration tip:** Record a few minutes of a known resistive load (through safe isolation). Derive scale factors for V/I/P in software. Never expose the microcontroller to mains potential.
