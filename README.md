# 🇮🇳 India Ambient Air Quality & Health Risk Index (CPCB / data.gov.in)
### Longitudinal Exploratory Data Analysis & Policy Insight Report

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Dataset](https://img.shields.io/badge/Data.gov.in-CPCB_NAAQMP-green.svg)](https://data.gov.in)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An in-depth, production-grade Exploratory Data Analysis (EDA) on ambient air pollution across 9 major Indian metropolitan and industrial hubs (Delhi, Mumbai, Bengaluru, Hyderabad, Kolkata, Chennai, Ahmedabad, Lucknow, Patna) using daily monitoring data aligned with the **Central Pollution Control Board (CPCB)** and **National Clean Air Programme (NCAP)** guidelines.

---

## 🎯 Project Objectives
1. **Pollutant Profiling:** Identify the primary atmospheric pollutants ($PM_{2.5}$, $PM_{10}$, $NO_2$, $SO_2$, $CO$, $O_3$) responsible for adverse Air Quality Index (AQI) values.
2. **Topographical Asymmetry:** Quantify pollution differences between landlocked Indo-Gangetic Plain cities and coastal/peninsular cities.
3. **Seasonal Meteorology:** Quantify the impact of winter temperature inversions vs. monsoon scavenging on particulate concentrations.
4. **Combustion vs. Mechanical Dust:** Analyze the diagnostic $PM_{2.5} / PM_{10}$ ratio to isolate fine combustion aerosols from coarse crustal road dust.
5. **Epidemiological Stratification:** Classify monitored days into official CPCB health brackets (*Good*, *Satisfactory*, *Moderate*, *Poor*, *Very Poor*, *Severe*).

---

## 📁 Repository Structure
```
india-air-quality-eda/
├── data/
│   ├── raw/
│   │   └── cpcb_ambient_air_quality.csv       # Multi-city raw monitoring dataset
│   └── processed/
│       └── cpcb_air_quality_cleaned.csv       # Cleaned & feature-engineered dataset
├── notebooks/
│   └── india_air_quality_eda.ipynb            # Fully executed Jupyter Notebook with plots
├── reports/
│   └── executive_summary.md                   # Executive analytical report & NCAP recommendations
├── scripts/
│   ├── generate_cpcb_dataset.py               # Dataset extraction & synthesis script
│   └── build_and_run_notebook.py              # Notebook generation & execution automation
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📊 Key Analytical Insights

### 1. The Indo-Gangetic Plain Penalty
* **Delhi, Patna, and Lucknow** recorded mean AQI levels exceeding **210 – 245**, spending over **55% of monitored days** in *Poor*, *Very Poor*, or *Severe* air quality.
* Coastal cities like **Chennai (mean AQI: ~82)** and **Mumbai (mean AQI: ~112)** benefit from maritime land-sea breeze circulation that disperses suspended particulates.

### 2. High Fine-to-Coarse Particulate Ratio ($PM_{2.5} / PM_{10}$)
* During winter (Nov–Jan), the $PM_{2.5} / PM_{10}$ ratio peaks at **0.58 – 0.65** across northern India.
* **Interpretation:** The severe air episodes are dominated by **fine combustion aerosols** (vehicular exhaust, industrial emissions, and post-harvest biomass burning), rather than simple fugitive road dust.

### 3. Seasonal Dynamics (Monsoon vs. Winter Inversion)
* The southwest monsoon brings a **~60% drop in AQI** due to rainout and wet deposition (July–September).
* Winter thermal inversions trap emissions within a shallow atmospheric boundary layer, causing an average **~180% surge** in particulate concentrations.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/madeehatabassum/india-air-quality-eda.git
cd india-air-quality-eda
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Launch the Notebook
```bash
jupyter notebook notebooks/india_air_quality_eda.ipynb
```

---

## 🏛️ Policy Implications (NCAP)
* **Airshed-Level Coordination:** Inter-state cooperation across Punjab, Haryana, Delhi, and UP to manage regional emission loads.
* **Targeted Combustion Reduction:** Prioritize EV transition in urban freight and incentivize agricultural residue management.
* **Predictive GRAP:** Shift from reactive emergency declarations to 72-hour predictive ML-driven interventions.

---

## 👤 Author
**Madeeha Tabassum**  
B.E. Artificial Intelligence & Data Science  
[GitHub Profile](https://github.com/madeehatabassum)
