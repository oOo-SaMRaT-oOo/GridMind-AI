# GridMind AI: ⚡ Predict. Protect. Stabilize.
GridMind AI is an engineering-grade, machine learning-driven framework designed to continuously monitor power grid frequency response behavior and forecast collapse risks before critical stability thresholds are breached. Developed as an end-to-end analytics platform, the system bridges the gap between complex power system dynamics and operator decision support by transforming real-time metrics into actionable early-warning insights.

---

## System Overview

Modern power systems face significant stability challenges due to high penetration of renewable energy sources and low rotational inertia. GridMind AI mitigates these risks by leveraging a trained machine learning model that analyzes engineered frequency features in real-time.

The architecture consists of three core domains:
1. **Dynamic Power System Simulation:** A Simulink model (`simulink_model.slx`) that simulates grid contingencies, load-shedding events, and frequency excursions to generate high-fidelity physical data (`.mat` files).
2. **Machine Learning Pipeline:** A Jupyter Notebook pipeline (`ML_Model.ipynb`) that extracts transient stability indicators, handles feature engineering, trains a Random Forest Classifier, and exports the serialized model (`GridMind_AI.pkl`).
3. **Operational Vision Terminal:** A dynamic Streamlit web application (`webapp.py`) engineered with a high-visibility, professional sci-fi industrial user interface to replay operational data and display real-time probability curves and feature animations.

---

## Feature Engineering and Metrics

The system processes raw frequency deviations ($df$) and time vectors to derive high-order statistical and physical features critical for predicting transient grid collapse:

* **Frequency Change ($df$):** The primary deviation from the nominal operating frequency.
* **Rate of Change of Frequency (RoCoF):** The first derivative of frequency deviation over time ($\frac{df}{dt}$), indicating the initial velocity of the disturbance.
* **Frequency Acceleration:** The second derivative of frequency deviation over time ($\frac{d^2f}{dt^2}$), reflecting the rate of change of structural electrical stress.
* **Cumulative Drop (Electrical Stress):** An exponentially weighted moving average (EWMA) tracking the integrated area of frequency degradation over time to capture sustained grid stress.
* **RoCoF Variance:** A rolling variance of RoCoF values over short windows, highlighting rapid micro-fluctuations and system jitter.
* **RoCoF Elasticity:** The ratio of Frequency Acceleration to RoCoF ($\frac{\text{Acceleration}}{\text{RoCoF}}$), quantifying the structural compliance or stiffness of the grid under load changes.

---

## Repository Structure

```text
├── ML_Model.ipynb               # Jupyter Notebook for ML model training, evaluation, and serialization
├── simulink_model.slx           # MATLAB/Simulink physical model for frequency response simulation
├── webapp.py                    # Main execution script for the Streamlit web dashboard
├── functions_styles/
│   ├── functions.py             # Feature extraction and mathematical processing algorithms
│   └── styles.py                # Specialized UI style sheets and custom web components
└── sidebar_pages/
    ├── vision_terminal.py       # Real-time monitoring terminal displaying AI metrics and curves
    ├── system_objectives.py     # Structural framework documentation page
    └── about_author.py          # Creator profile page

```

---

## Installation and Setup

### Prerequisites

Ensure that Python 3.8+ and MATLAB/Simulink are installed on your workstation.

### Step 1: Clone the Repository

```bash
git clone [https://github.com/yourusername/GridMind-AI.git](https://github.com/yourusername/GridMind-AI.git)
cd GridMind-AI

```

### Step 2: Install Dependencies

Install the required analytical and web-rendering libraries:

```bash
pip install numpy pandas matplotlib scipy scikit-learn joblib streamlit

```

### Step 3: Run the Machine Learning Pipeline (Optional)

If you wish to retrain the underlying model or explore the data distribution, execute the Jupyter Notebook:

```bash
jupyter notebook ML_Model.ipynb

```

This notebook extracts variables from your Simulink `.mat` telemetry logs, performs a group-stratified K-Fold cross-validation, generates classification matrices, and serializes the state to `GridMind_AI.pkl`.

### Step 4: Launch the Operational Terminal

Execute the Streamlit server to deploy the interactive operator control interface:

```bash
streamlit run webapp.py

```

---

## Machine Learning & Classification Pipeline

The underlying intelligence uses a **Random Forest Classifier** validated via a `GroupKFold` cross-validation strategy. This ensures that the model is tested on independent, unseen contingency event profiles rather than random timeline frames, eliminating look-ahead bias and mathematical leakage.

* **Inputs:** Data frames containing $df$, RoCoF, Frequency Acceleration, Cumulative Drop, RoCoF Variance, and RoCoF Elasticity.
* **Output:** A calibrated probability distribution classifying the system state into either `Stable / Recovery State (0)` or `Imminent Grid Collapse (1)`.
* **Deployment State:** Serialized into an optimized binary format via `joblib` for sub-millisecond prediction latency inside the execution loop.

---

## Interface & User Experience

The application is styled as a professional, mission-critical operations deck featuring:

* **High-Contrast Digital Metrics:** Real-time delta updates evaluating current frames against historical time steps.
* **Dynamic Probability Trajectories:** Line charts tracking the continuous fluctuation of risk percentage points.
* **Electrical Jitter Indicators:** Interactive widgets highlighting anomalies in system inertia and mechanical stress response.

---

## Project Context

GridMind AI was designed and engineered by **Samrat Malla**, an Electrical Engineering student at the Pulchowk Campus. The project demonstrates the practical convergence of machine learning, power system physics, and real-time operations software to build smarter, more resilient energy grids.

---

## 📸 System Showcase & Visual Interface

<p align="center">
   <img src="assets/1.jpg" alt="GridMind AI Operation Front Page" width="70%">

</p>

---

## 📊 2. System Rundown (Analysis)
A deep-dive workspace breakdown displaying the exact operational transition of the telemetry tower when an anomaly breaches grid tolerances.

<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="50%" align="center" valign="top">
        <strong>🟢 SYSTEM RUNDOWN</strong><br><br>
        <img src="assets/4.jpg" alt="Healthy System State" width="100%">
        <img src="assets/3.jpg" alt="Healthy System State" width="100%">
      </td>
      <td width="50%" align="center" valign="top">
        <strong>🟢 Quantity Measurments</strong><br><br>
        <img src="assets/5.jpg" alt="Tripped Breaker State" width="100%">
        <img src="assets/6.jpg" alt="Tripped Breaker State" width="100%">
      </td>
    </tr>
  </table>
</div>

<br>

---








