# Smart_Energy_Monitoring

# Project Title
*Smart Energy Monitoring for Indian Hospitals*

## 📅 Project Timeline

- **Duration:** 10 August 2010 – 8 October  2010(Part-Time)  
- **Acadamic Year:** 1st year of Electrical and Electronics Engineering
- **Location:** VIT University, Vellore, India 



## 📌 Objective
Constructed a low-cost, Internet of Things-based system to monitor and optimise energy consumption in a hospital ward in India, minimising waste and peak load.

⚠️ Disclaimer

This project was originally built in 2010 as part of academic research at VIT University. which is part time project.

Modernisation note: This project was originally built in Aug–Oct 2010. In Sep 2025, I uploaded the code to GitHub and refreshed it to run on current tooling (Python 3.11; added mock‑based tests, CI and metrics). Commit dates reflect publication/cleanup, not the original build period.

The RS485 serial communication code in this project communicates with particular hardware devices that are attached to a serial port (/dev/ttyUSB0).

Crucial Information:

For the code to function properly, an RS485 adapter or other appropriate device must be attached.

Running this code in Continuous Integration (CI) will likely fail since CI systems (including GitHub Actions) cannot access actual hardware.

The repository is kept open to highlight:

Python (pyserial) handling of serial communication

Methods for data gathering and logging

Workflow examples for tasks involving hardware

Suggestion:

The script must be executed on a local machine with the relevant RS485 hardware attached in order to function properly.

To replicate hardware input without requiring real devices, consider mocking the serial interface for automated runs or CI testing.

## 📊 Repository Health

This project is under continuous improvement.  
An [Audit Report](../../issues/1) has been created to track repository health and enhancements:  
- Releases & versioning (to be added)  
- Expanded test coverage (planned with `pytest`)  
- Metrics/artifacts integration (CSV/PNG export in CI)  



## 🏥 Background & Relevance
Due to ineffective HVAC control, lighting, and machine idle, Indian hospitals frequently waste energy. 
The goal of this research was to enable focused interventions by measuring and analysing consumption in real time.

## Modules Covered
| **Module**                                            | **Application in Project**                                                                             |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------                           |
| **Computer Programming and Problem Solving**          | Arduino coding in C/Embedded C, Python for data analysis, MATLAB scripts for simulations.              |
| **English for Engineers – I**                         | Technical documentation, report writing, and presentation of project findings.                         |
| **Multivariable Calculus and Differential Equations** | Modeling energy consumption patterns, load variation, and analyzing HVAC dynamics.                     |
| **Engineering Graphics**                              | Drafting the layout of hospital wards, sensor placements, and circuit diagrams.                        |
| **Workshop Practice**                                 | Assembling circuits, soldering sensors, and creating hardware prototypes.                              |
| **Modern Physics**                                    | Understanding sensor physics (CT sensors, electromagnetic induction) for accurate current measurement. |


## ⚙️ Methodology
Arduino Uno with CT sensors for current measurement

RS-485 communication to central PC

Data logging in CSV format

MATLAB Simulink model for load profile analysis

Simulation using Tamil Nadu Electricity Board tariff data

## ⚡ Quick Start — Run in 3 Commands

1. **Create & activate environment**  
   ```bash
   conda env create -f environment.yml
   conda activate smart-energy
2. **Run the demo pipeline**
   python demo/demo_signal_pipeline.py

3. **View generated plots and metrics**
   Plots: results/plots/
   Metrics CSV: results/metrics.csv

## 📂 Data Sources
- **Source 1:** Bureau of Energy Efficiency (BEE) Hospital Audit Reports 2010 – India -  https://www.beeindia.gov.in/ergydata.php
- **Source 2:** Tamil Nadu EB Tariff Schedule + [link](https://www.tnerc.tn.gov.in/raw_data_2010.php)  



## 🛠️ Tools & Technologies
- MATLAB / Simulink
- Arduino IDE
- Python / C / Embedded C
- Excel / Power BI / Data visualization tools

---

## 📊 Results
- Identified 15% potential savings by rescheduling HVAC and lighting loads
- <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/b6783a38-944e-4428-823b-943f4fc6dd1d" />
<img width="982" height="662" alt="image" src="https://github.com/user-attachments/assets/aa727676-29fd-4796-8d15-67e644869eea" />


- Visualized hourly energy consumption in MATLAB

## Contact  
For questions, collaboration, or feedback, please contact:  
**Sammeta Dinesh Kumar** — [sammetadineshkumar@gmail.com]
- 🌐 [Portfolio](https://dineshkumarsammeta.github.io/)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/dineshsammeta)   

