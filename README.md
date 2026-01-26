# 🌿 5G Eco-RAN: "Zero-Bit, Zero-Watt" Optimization Engine

> **Status:** 🚧 Active Development (Architecture Phase)
> **Focus:** AI Strategy | Network Sustainability | Predictive Analytics

## 🎯 The Business Problem
Telecommunications networks face a critical efficiency paradox: **Base stations consume 80-90% of their peak energy even when carrying zero traffic.** For a major carrier like T-Mobile, this "always-on" inefficiency represents:
1.  **High OPEX:** Massive electricity costs for idle hardware.
2.  **Sustainability Gap:** A barrier to achieving "Net Zero" carbon targets.

## 💡 The Strategy: Intelligent Sleep Modes
This project builds a **Predictive Control System** that forecasts cellular traffic at the base-station level. By accurately predicting "dead zones" (periods of low traffic), the system dynamically powers down antenna arrays without degrading User Experience (UX).

**Projected Impact:**
* **Target:** Reduce energy consumption by 15-20% during off-peak hours.
* **Constraint:** Maintain 99.99% service availability (no dropped calls).

## 🛠️ Technical Architecture
The system is designed as a modular Python pipeline:

* **Data Source:** NetOp 5G Energy Consumption Dataset (Hugging Face)
    * *Input:* Traffic Load (Erlangs), Bandwidth, Antennas.
    * *Target:* Energy Consumption (kWh).
* **Model:** XGBoost Regressor (Gradient Boosting) for time-series forecasting.
* **Policy Engine:** Logic layer that translates "Low Traffic Prediction" into "Sleep Mode Action."

## 📂 Current Progress
- [x] **Environment Setup:** Python, Pandas, XGBoost pipeline established.
- [x] **Simulation Layer:** Synthetic data generator created to model load/energy relationships.
- [ ] **Data Ingestion:** Awaiting access approval for NetOp research data.
- [ ] **Model Training:** Hyperparameter tuning on real-world 5G logs.
- [ ] **ROI Dashboard:** Visualization of energy savings vs. potential latency cost.

## 🚀 Quick Start (Simulation Mode)
While waiting for the research dataset, you can run the **simulation engine** to see the logic in action:

```bash
# 1. Clone the repo
git clone [https://github.com/yourusername/5g-energy-optimization.git](https://github.com/yourusername/5g-energy-optimization.git)

# 2. Install dependencies
pip install pandas numpy xgboost seaborn matplotlib

# 3. Run the simulation
python main.py --mode simulation
