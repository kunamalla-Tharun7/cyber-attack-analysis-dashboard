# 🛡️ Global Cyber Attack Data Analysis Dashboard

An end-to-end data analysis project that explores global cyber attack patterns using **Python**, **MySQL**, and **Streamlit**. The dashboard gives security analysts and stakeholders a clear, visual view of which countries are most targeted, which industries are most at risk, how attacks have evolved over time, and what the financial consequences look like.

---

## 📸 Screenshots

> After running the app, screenshots will look something like this:

| KPI Summary | Country Chart |
|---|---|
| Total attacks, loss, records stolen | Top 10 attacked countries |

| Industry Chart | Trend Line |
|---|---|
| Most targeted sectors | Attack growth by year |

---

## 🎯 Project Overview

This project answers five key questions:

1. **Which countries** are attacked most frequently?
2. **Which industries** are the most vulnerable?
3. **How have attacks changed** year over year?
4. **Which attack types** cause the most financial damage?
5. **How many records** are stolen per attack category?

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Database | MySQL 8.0 |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib |
| Dashboard | Streamlit |
| Configuration | python-dotenv |

---

## 📂 Project Structure

```
cyber-attack-analysis/
│
├── dataset/
│   └── cyber_attacks.csv          # 5,000-row synthetic dataset
│
├── sql/
│   └── create_tables.sql          # DB schema + analytical views
│
├── python/
│   ├── database_connection.py     # MySQL connection manager
│   ├── load_data.py               # CSV → MySQL loader
│   └── analysis.py                # All queries + chart functions
│
├── dashboard/
│   └── app.py                     # Streamlit dashboard
│
├── outputs/                       # Auto-created; stores saved PNGs
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The dataset (`cyber_attacks.csv`) contains **5,000 simulated cyber attack records** with the following fields:

| Column | Type | Description |
|---|---|---|
| `attack_id` | INT | Unique identifier |
| `country` | VARCHAR | Target country |
| `industry` | VARCHAR | Targeted sector |
| `attack_type` | VARCHAR | Type of cyber attack |
| `year` | INT | Year attack occurred (2015–2024) |
| `financial_loss` | FLOAT | Estimated loss in million USD |
| `records_stolen` | BIGINT | Number of records compromised |

---

## 🗄️ Database Schema

```sql
CREATE TABLE cyber_attacks (
    attack_id      INT            NOT NULL,
    country        VARCHAR(50)    NOT NULL,
    industry       VARCHAR(50)    NOT NULL,
    attack_type    VARCHAR(50)    NOT NULL,
    year           INT            NOT NULL,
    financial_loss DECIMAL(10,2)  NOT NULL,
    records_stolen BIGINT         NOT NULL,
    PRIMARY KEY (attack_id),
    INDEX idx_country     (country),
    INDEX idx_industry    (industry),
    INDEX idx_attack_type (attack_type),
    INDEX idx_year        (year)
);
```

Four analytical **views** are also created:
- `vw_attacks_by_country`
- `vw_attacks_by_industry`
- `vw_attacks_by_year`
- `vw_loss_by_attack_type`

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cyber-attack-analysis.git
cd cyber-attack-analysis
```

### 2. Create and activate a virtual environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Open .env and fill in your MySQL credentials
```

Your `.env` should look like:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cyber_attack_db
```

---

## 🗄️ Database Setup

### Step 1 — Create the database and table

Open MySQL Workbench (or any MySQL client) and run:

```bash
mysql -u root -p < sql/create_tables.sql
```

Or paste the contents of `sql/create_tables.sql` directly into MySQL Workbench and execute.

### Step 2 — Load the dataset into MySQL

```bash
python python/load_data.py
```

Expected output:
```
──────────────────────────────────────────────────
  Cyber Attack Data Loader
──────────────────────────────────────────────────
Reading dataset: .../dataset/cyber_attacks.csv
  Rows loaded from CSV : 5,000
Connecting to MySQL …
Inserting records …
  Rows inserted        : 5,000
Done ✓
──────────────────────────────────────────────────
```

### Step 3 — (Optional) Generate static charts

```bash
python python/analysis.py
```

Charts are saved to the `outputs/` folder.

---

## 📊 Run the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Then open your browser at **http://localhost:8501**

The dashboard includes:
- 📊 **KPI row** — total attacks, countries affected, financial loss, records stolen
- 🌍 **Top Attacked Countries** — horizontal bar chart
- 🏭 **Most Targeted Industries** — vertical bar chart
- 📈 **Attack Trend by Year** — line chart with area fill
- 💸 **Financial Loss by Attack Type** — horizontal bar chart
- 📁 **Records Stolen** — pie chart + breakdown table
- 🔍 **Search & Filter** — filter by year, industry, attack type; search raw data

---

## ✨ Features

- ✅ Dark Netflix-inspired UI theme
- ✅ Sidebar filters (year, industry, attack type)
- ✅ Live data from MySQL (5-minute cache)
- ✅ Interactive search across all records
- ✅ All charts generated with Matplotlib — no external chart libs
- ✅ Modular, production-quality Python code
- ✅ Environment variables for credentials (never hardcoded)

---

## 🔮 Future Improvements

- [ ] Add geographic heatmap using Plotly or Folium
- [ ] Connect to a live threat intelligence API (e.g., VirusTotal, Shodan)
- [ ] Add ML-based attack prediction using scikit-learn
- [ ] Export filtered data as CSV from the dashboard
- [ ] Add user authentication for the dashboard
- [ ] Deploy to Streamlit Cloud or AWS EC2

---

## 👨‍💻 Author

Built as a portfolio project demonstrating end-to-end data engineering skills:
data generation → SQL database design → Python analysis → interactive dashboard.

---

## 📄 License

MIT License — free to use, modify, and distribute.
