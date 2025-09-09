# 📂 Data Provenance & Policy

This document outlines the sources, licenses, and handling policies for data used in the **Smart Energy Monitoring** project.

---

## 1. Real Data Sources

| Data Source | Type | License | Link |
| ----------- | ---- | ------- | ---- |
| Bureau of Energy Efficiency (BEE) | Hospital energy audit reports (India) | Public / Government | [BEE Reports](https://www.beeindia.gov.in/ergydata.php) |
| Tamil Nadu Electricity Board Tariff Schedule | Historical electricity tariffs | Public / Government | [TNERC Data](https://www.tnerc.tn.gov.in/raw_data_2010.php) |

**Notes:**  
- Real datasets are used for research and demonstration purposes only.  
- Sensitive information has been anonymized.  

---

## 2. Synthetic Sample Data

- A **synthetic dataset** (`data/sample.csv`) is provided for testing and CI purposes.  
- The synthetic data mimics the structure and types of the real data but contains **no sensitive information**.  
- Example columns:  
  - `timestamp` – datetime of measurement  
  - `load_kW` – energy consumption in kW  
  - `device_id` – anonymized ID  

**Purpose:**  
- Enables testing CI workflows without needing access to real hardware or sensitive data.  
- Allows recruiters, collaborators, and CI pipelines to run scripts reproducibly.  

---

## 3. Data Use Policy

1. **Real Data**  
   - Only use for research, educational, and development purposes.  
   - Do not redistribute sensitive or personally identifiable information.  

2. **Synthetic Data**  
   - Free to use for testing, CI, or demo purposes.  
   - Can be shared publicly in GitHub without license restrictions.  

---

## 4. Attribution & Licenses

- Government / public datasets: Attribution required if used in reports or publications.  
- Synthetic datasets: No restrictions.  

---

> ⚠️ Disclaimer: Scripts using real RS485 data require appropriate hardware and access to real datasets. CI runs use synthetic data and mocks for demonstration.
