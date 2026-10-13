# 📋 Executive Analytical Summary: India Ambient Air Quality EDA

**Author:** Madeeha Tabassum  
**Target:** Environmental Policy Teams, Public Health Analysts & Data Science Recruiters  
**Data Provenance:** Central Pollution Control Board (CPCB), Ministry of Environment, Forest & Climate Change (MoEFCC), via [data.gov.in](https://data.gov.in)  
**Longitudinal Period:** 2021 – 2024 Daily Monitoring Across 9 Metropolitan Centers  

---

## 1. Context & Motivation
Under India's **National Clean Air Programme (NCAP)**, the Government of India established aggressive targets to achieve a **20% to 40% reduction in $PM_{2.5}$ and $PM_{10}$ concentrations** by 2026 across non-attainment cities. This project delivers an empirical Exploratory Data Analysis (EDA) of longitudinal ambient air quality data published on `data.gov.in`.

---

## 2. Quantitative Key Findings

| Finding | Metric / Evidence | Significance |
| :--- | :--- | :--- |
| **Indo-Gangetic Airshed Penalty** | Delhi, Patna & Lucknow mean AQI: **210 – 245** | Topographic containment between Himalayas & Vindhyas prevents atmospheric dispersion. |
| **Maritime Cleansing Dividend** | Chennai & Mumbai mean AQI: **75 – 115** | Dynamic sea-breeze convection maintains particulate levels within NAAQS thresholds for ~70% of days. |
| **Combustion vs. Crustal Dust** | Winter $PM_{2.5} / PM_{10}$ ratio: **0.58 – 0.65** | Elevated fine particulate ratio confirms vehicular and biomass combustion as the dominant driver, not crustal road dust. |
| **Seasonal Vulnerability Window** | Nov–Jan AQI spike: **+180%** vs. July–Aug | Severe thermal boundary layer compression requires scheduled emergency intervention windows. |

---

## 3. Epidemiological Risk Stratification
Using official CPCB breakpoint criteria:
* **Severe Exposure Zone (Delhi, Patna, Lucknow):** Over **55% of monitored days** fell into *Poor*, *Very Poor*, or *Severe* categories ($AQI > 200$).
* **Safe / Moderate Zone (Bengaluru, Chennai, Hyderabad):** Over **85% of monitored days** remained within *Good*, *Satisfactory*, or *Moderate* categories ($AQI \le 200$).

---

## 4. Policy Roadmap & Technical Recommendations
1. **Air-Shed Regional Governance:** Shift from isolated city municipal action plans to unified airshed emission capping councils spanning Punjab, Haryana, Delhi, and Uttar Pradesh.
2. **Targeted Micro-Source Mitigation:** Address fine aerosol emissions ($PM_{2.5}$) via localized industrial transition to piped natural gas (PNG) and targeted EV fleet transitions in logistics corridors.
3. **Automated Early Warning Systems:** Deploy 72-hour forecasting pipelines to trigger Graded Response Action Plan (GRAP) tiers proactively.
