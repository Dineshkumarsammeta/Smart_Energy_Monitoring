# Smart_Energy_Monitoring

# Project Title
*Smart Energy Monitoring for Indian Hospitals*

## 📅 Project Timeline
**Duration:** August 2010 – October  2010  
**Location:** VIT University, Vellore, India 


## 📌 Objective
Constructed a low-cost, Internet of Things-based system to monitor and optimise energy consumption in a hospital ward in India, minimising waste and peak load.

⚠️ Disclaimer

The RS485 serial communication code in this project communicates with particular hardware devices that are attached to a serial port (/dev/ttyUSB0).

Crucial Information:

For the code to function properly, an RS485 adapter or other appropriate device must be attached.

Running this code in Continuous Integration (CI) will probably fail since CI systems, including GitHub Actions, are unable to access actual hardware.

The repository is kept open to the public for demonstration and instructional purposes in order to highlight:

Python (pyserial) handling of serial communication

Methods for data gathering and logging

Workflow example for tasks involving hardware

Suggestion:

The script must be executed on a local computer with the relevant RS485 hardware attached in order to function properly.

To replicate hardware input without the need for real devices, think about mocking the serial interface for automated runs or continuous integration testing.

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

- Visualized hourly energy consumption in MATLAB
- 
## Contact  
For questions, collaboration, or feedback, please contact:  
**Sammeta Dinesh Kumar** — [sammetadineshkumar@gmail.com]
- 🌐 [Portfolio](https://dineshsammeta1234.github.io/)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/dineshsammeta)   

