# 📊 CODTECH IT Solutions — Data Analytics Internship
## Task 3: Dashboard Development

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Interactive%20Dashboard-008DE4?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

## 🏢 Internship Details

| Field | Details |
|---|---|
| **Company** | CODTECH IT Solutions Pvt. Ltd. |
| **Intern Name** | Abhijeet Das |
| **Intern ID** | CITS500 |
| **Domain** | Data Analytics |
| **Task** | Task 3 — Dashboard Development |
| **Duration** | 4 Weeks |
| **Mentor** | Neela Santhosh Kumar |

---


## 🎯 Project Overview

> Create a **fully functional interactive dashboard** using **Dash (Python)** to visualize a sales dataset with actionable business insights. The dashboard includes live filters, KPI cards, and 8 interactive charts — all updating in real time.

---

## 🗂️ Project Structure

```
Task-3-Dashboard-Development/
│
├── 📄 dashboard.py       ← Main Dash application
├── 📊 sales_data.csv     ← Dataset (500 records)
└── 📝 README.md
```

---

## 📊 Dataset

**File:** `sales_data.csv` | **Records:** 500 rows × 17 columns  
Covers 3 years (2021–2023) of Indian retail sales across 5 categories, 4 regions, and 3 customer segments.

---

## 🛠️ Tools & Libraries

| Library | Purpose |
|---------|---------|
| **Dash** | Interactive web dashboard framework |
| **Plotly** | Interactive charts and graphs |
| **Pandas** | Data loading and processing |

---

## 🔧 How to Run

### Step 1 — Install dependencies
```bash
pip install dash plotly pandas
```

### Step 2 — Run the dashboard
```bash
python dashboard.py
```

### Step 3 — Open in browser
```
http://127.0.0.1:8050
```

---

## 📊 Dashboard Features

### 🎛️ Live Filters (4 dropdowns)
| Filter | Options |
|--------|---------|
| Year | 2021, 2022, 2023, All |
| Category | Electronics, Clothing, Furniture, Groceries, Sports |
| Region | North, South, East, West |
| Segment | Consumer, Corporate, Home Office |

> All charts and KPIs update instantly when any filter changes.

### 📌 KPI Cards (5 metrics)
- Total Sales (₹)
- Total Profit (₹) with margin %
- Total Orders count
- Average Order Value
- Profit Margin %

### 📈 8 Interactive Charts
| Chart | Type | Insight |
|-------|------|---------|
| Monthly Sales & Profit Trend | Line chart | Seasonal patterns |
| Sales by Category | Horizontal bar | Top categories |
| Sales by Region | Donut pie | Regional share |
| Sales vs Profit Scatter | Bubble chart | Profitability by category |
| Sales by Customer Segment | Donut pie | Segment contribution |
| Category × Quarter Heatmap | Heatmap | Seasonal category trends |
| Top 10 Products | Horizontal bar | Best sellers |

---

## 🖥️ Dashboard Preview

```
┌─────────────────────────────────────────────────┐
│  📊 Sales Analytics Dashboard    CODTECH        │
├─────────────────────────────────────────────────┤
│  Filters: [Year ▼] [Category ▼] [Region ▼] ...  │
├─────────────────────────────────────────────────┤
│ ₹Total Sales │ ₹Profit │ Orders │ AOV │ Margin  │
├──────────────────────┬──────────────────────────┤
│  Monthly Trend       │   Category Bar Chart     │
├────────┬─────────────┴──────────────┬───────────┤
│ Region │    Profit Scatter          │  Segment  │
├────────┴────────────────────────────┴───────────┤
│   Category × Quarter Heatmap  │  Top Products   │
└─────────────────────────────────────────────────┘
```

---

## 🔑 Key Actionable Insights

1. **Electronics** generates the highest revenue across all regions
2. **Q3 and Q4** consistently show peak sales — holiday season effect
3. **North region** leads in total sales contribution
4. **Consumer segment** accounts for majority of orders
5. Higher discounts correlate with lower profit margins
6. **Corporate segment** has the highest average order value

---

<div align="center">
<b>CODTECH IT Solutions Pvt. Ltd.</b> — Data Analytics Internship — Task 3
</div>
