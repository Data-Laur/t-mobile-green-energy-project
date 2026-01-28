# Project Zero-Watt: AI-Driven 5G Energy Optimization 🌿⚡

**Reducing Telecommunications Carbon Footprint via XGBoost Traffic Prediction**

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Model](https://img.shields.io/badge/Model-XGBoost-orange)
![Status](https://img.shields.io/badge/Status-Complete-green)

## Executive Summary
**The Problem:** 5G towers are energy-intensive assets, often running at full static power (300W+) 24/7, even during deep night hours when user traffic is near zero. This results in massive OpEx waste and unnecessary carbon emissions.

**The Solution:** "Project Zero-Watt" is a Machine Learning pipeline that predicts network traffic 24 hours in advance. By identifying "Deep Sleep" windows with high confidence, the system dynamically lowers power consumption without risking dropped calls.

**Key Impact:**
* **25% Reduction** in daily energy consumption per tower.
* **< 4% Error Rate** (MAE) ensuring network reliability.
* **Validated** using a Physics-Based Digital Twin simulation.

---

## Visual Impact

### 1. The Result: Eliminating "Idle Waste"
*The AI identifies the low-traffic window (1 AM - 5 AM) and safely lowers power, saving ~5 kWh per day per tower.*

![Energy Savings Graph]([/images/Viz 4: Project Impact.png](https://github.com/user-attachments/assets/11461cb1-a3af-4e0b-80e3-57e75f5a692a))

### 2. The Logic: Why the Model Works
*Feature importance analysis reveals that network traffic is highly habitual. The model relies heavily on "Yesterday's Traffic" (Lag24) to predict today's load.*

![Feature Importance Graph](/images/Viz 3: Model Logic (Feature Importance).png)

---

## 🛠️ Methodology

### 1. Data Simulation (The Digital Twin)
Due to the proprietary nature of real-world telecom data, I engineered a **Physics-Based Digital Twin** to generate realistic 5G telemetry.
* **Schema:** Modeled after standard Huawei/Ericsson energy consumption logs.
* **Physics:** Implemented linear power models ($P_{load} = P_{static} + \beta \cdot Load$).
* **Noise:** Injected stochastic noise and anomalies to stress-test the model.

### 2. Feature Engineering
The raw time-series data was transformed to capture temporal dependencies:
* **Lag Features:** `Load_Lag1` (Short-term trend), `Load_Lag24` (Daily seasonality).
* **Cyclical Encoding:** Sine/Cosine transformation for Hour of Day.
* **Rolling Statistics:** 3-hour moving averages to smooth volatile spikes.

### 3. Modeling Strategy (XGBoost)
I selected **XGBoost (Gradient Boosting)** over LSTM/RNNs for three reasons:
1.  **Inference Speed:** Critical for edge deployment on tower hardware.
2.  **Interpretability:** Tree-based feature importance allows engineers to audit decisions.
3.  **Performance:** Superior handling of tabular time-series data with distinct seasonality.

---

## How to Run

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/YourUsername/Project-Zero-Watt.git](https://github.com/YourUsername/Project-Zero-Watt.git)
