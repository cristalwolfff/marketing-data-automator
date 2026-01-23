# 📊 Marketing Intelligence Pipeline (ETL)
*(Automated Financial Analysis for Ad Campaigns)*

![Python](https://img.shields.io/badge/Core-Python_3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Data_Engineering_&_ETL-5C4EE5?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

> **"From Raw Data to Actionable Strategy."**
> A robust Python engine designed to eliminate manual Excel reporting by automating the ingestion, processing, and ranking of marketing campaign data.

---

## 🎯 The Business Problem
In digital marketing operations, analysts waste hours manually calculating metrics across fragmented spreadsheets. This legacy process creates:
1.  **Operational Bottlenecks:** Time spent calculating instead of strategizing.
2.  **Data Integrity Risks:** Human error in formulas (e.g., broken ROI calculations).
3.  **Latency:** Delays in identifying underperforming ads.

## 💡 The Engineering Solution
I engineered this script as a **lightweight ETL (Extract, Transform, Load) pipeline**.
It ingests raw campaign dictionaries, applies hard-coded business logic to calculate financial health, and outputs a ranked decision-support dashboard in the terminal.

---

## ⚙️ Core Architecture & Features

### 1. Business Logic Normalization (The "Transform" Layer)
The system implements standard financial models directly into the code structure:
* **CTR (Click-Through Rate):** Measures ad resonance (`Clicks / Impressions`).
* **CPA (Cost Per Acquisition):** Tracks efficiency (`Cost / Conversions`).
* **ROI (Return on Investment):** Calculates net profitability (`(Revenue - Cost) / Cost`).

### 2. Algorithmic Decision Support
* **Auto-Ranking:** The script doesn't just display numbers; it executes a sorting algorithm to identify the "Champion" campaign based on ROI.
* **Status Classification:** Automatically tags campaigns as `✅ Profit` or `🔻 Loss` based on financial thresholds.

### 3. Robust Error Handling
* **Zero-Division Protection:** Includes defensive coding to handle edge cases (e.g., campaigns with 0 impressions) without crashing the pipeline.

---

## 📸 Automated Output Demo
The system generates a clean, readable CLI dashboard for instant analysis:

```text
--- PROCESSING CAMPAIGN DATA BATCH ---

CAMPAIGN             | CTR        | ROI        | STATUS
------------------------------------------------------------
Black Friday Ads     | 5.00%      | 400.00%    | ✅ Profit
App Launch v2        | 1.50%      | -25.00%    | 🔻 Loss
Flash Sale Promo     | 8.00%      | 500.00%    | ✅ Profit
------------------------------------------------------------

🏆 PERFORMANCE CHAMPION: Flash Sale Promo (ROI: 500.00%)

```

---

## 🚀 How to Run (Zero-Dependency)

This tool was built with **Native Python 3**, requiring no external libraries (like Pandas) for easy deployment in restricted environments.

1. **Clone the repository:**
```bash
git clone [https://github.com/cristalwolfff/marketing-data-automator.git](https://github.com/cristalwolfff/marketing-data-automator.git)

```


2. **Navigate to directory:**
```bash
cd marketing-data-automator

```


3. **Run the Pipeline:**
```bash
python analisador.py

```



---

## 🛠️ Tech Stack

* **Python 3:** Core logic using Lists/Dictionaries, f-strings, and mathematical operators.
* **Business Logic:** Implementation of MarTech formulas (KPIs).

---

*Developed by [Cristalwolf](https://github.com/cristalwolfff) // AI & MarTech Engineer*

```
