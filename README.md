# Predictive Delivery Optimizer - NexGen Logistics

## 📋 Project Overview

A Streamlit-based predictive analytics dashboard that helps NexGen Logistics transform from reactive to predictive operations by forecasting delivery delays and suggesting corrective actions.

<img width="1905" height="796" alt="Image" src="https://github.com/user-attachments/assets/3fc48e70-1308-4db2-8adb-a672b3d016be" />

## 🚀 Features

### 1. **Executive Dashboard**
<img width="1472" height="721" alt="Image" src="https://github.com/user-attachments/assets/c8d346f2-b394-47ae-b1dc-d254eb17e9bf" />
- Real-time KPI metrics
- Interactive performance maps
- Delay rate visualization by priority
- Customer rating distribution

### 2. **Predictive Analytics**
<img width="1453" height="697" alt="Image" src="https://github.com/user-attachments/assets/2a7d081e-a749-4d16-9b18-42d5bb19a8d2" />
- Machine learning-based delay prediction
- Risk level classification (High/Medium/Low)
- Real-time order risk assessment
- Actionable recommendations

### 3. **Performance Analytics**
<img width="1529" height="785" alt="Image" src="https://github.com/user-attachments/assets/008f075d-d2e3-4b64-a7ba-93016908c89c" />

- Carrier performance comparison
- Weekly trend analysis
- Cost efficiency metrics
- Route optimization insights

### 4. **Data Export**
<img width="1526" height="698" alt="Image" src="https://github.com/user-attachments/assets/3d4cbb10-b60f-4fca-8d17-5b997c3982ab" />
- Export in CSV, Excel, JSON formats
- Filtered data downloads
- Scheduled reports

## 🛠️ Installation & Setup

### Prerequisites
![Python Logo](https://github.com/user-attachments/assets/759ee489-9919-4e07-8229-d4496e543265)
![Streamlit Logo](https://github.com/user-attachments/assets/1d29d091-9f46-4876-9b8c-42a84232ffdf)
- Python 3.8+
- pip package manager

### 🏗️ Architecture
Data Sources → Data Processing → ML Models → Dashboard → Actions/APIs
     ↓              ↓              ↓            ↓          ↓
   7 CSVs       Pandas/NumPy   Scikit-learn   Streamlit   Alerts
   APIs         Feature Eng.   Joblib Save    Plotly      Reports

### Step 1: Clone Repository
```bash
git clone https://github.com/shalr-20/Predictive-Delivery-Optimizer.git
cd Predictive-Delivery-Optimizer
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Add Your Data
Place the following CSV files in the data/ folder:
```bash
data/
├── orders.csv
├── delivery_performance.csv
├── routes_distance.csv
├── vehicle_fleet.csv
├── warehouse_inventory.csv
├── customer_feedback.csv
└── cost_breakdown.csv
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

## 🏗️ Architecture
<img width="676" height="131" alt="Image" src="https://github.com/user-attachments/assets/71c2449c-ee80-4e48-a37c-67441b1bbc1d" />
