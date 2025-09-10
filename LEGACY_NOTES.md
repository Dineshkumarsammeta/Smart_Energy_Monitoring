

# Smart Energy Monitoring — Legacy Notes (2010)

## Project Era
**Duration:** August 2010 – October 2010 (Part-Time)  
**Acadamic Year** First year of Electrical and Electronic Engineering
**Location:** VIT University, Vellore, India  

The hardware, software, and library versions utilised for the first project are documented in this page.  
The legacy arrangement is meant to be preserved for archiving purposes.

---

## 1. MATLAB / Simulink Environment
- **MATLAB Version:** R2009b – R2010a  
- **Simulink Version:** 7.0 (MATLAB R2009b compatible)  
- **Toolboxes Used:**  
  - Signal Processing Toolbox  
  - MATLAB Excel Import/Export functions  

**Notes:**  
- All scripts were developed and tested on Windows XP / MATLAB R2009b.  
- `.m` and `.mdl` files are legacy and may require updating for modern MATLAB releases.  

---

## 2. Arduino Environment
- **Arduino IDE Version:** 0017 – 0020 (2010 era)  
- **Board:** Arduino Uno (ATmega328P)  
- **Libraries Used:**  
  - RS485 / Modbus communication library (custom or early Modbus-Arduino variant)  
  - CT sensor readout library (custom voltage/current scaling functions)  

**Notes:**  
- Sensor calibration constants were hard-coded in Arduino sketches.  
- RS-485 communication was implemented via a MAX485 module.  
- Serial baud rate: 9600 bps  

---

## 3. Hardware Details
- **Current Transformer (CT) Sensors:** YHDC SCT-013-000 (or equivalent)  
- **RS-485 Adapter:** MAX485-based communication to PC  
- **PC Interface:** Serial-to-USB adapter (/dev/ttyUSB0 in Linux)  
- **Data Logging:** CSV export via Python scripts (legacy Python 2.6–2.7)  

---

## 4. Notes on Reproducibility
- Original code may not run on modern MATLAB / Arduino IDE without modifications.  
- Legacy libraries may need to be manually sourced or rewritten.  
- Modernized version (2025) uses:
  - Python 3.11
  - `pyserial` for RS-485 mocking
  - Reproducible CI environment via `pyproject.toml` and demo scripts

---

## 5. References
- Tamil Nadu Electricity Board tariff data (2010)  
- Bureau of Energy Efficiency (BEE) hospital energy audit reports (2010)  

