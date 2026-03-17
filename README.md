# Airline Ticket Price Analysis

Took a dataset with 250 airline tickets across 8 airlines and 8 cities and tried 
to figure out what actually affects the price — distance, airline, class, 
or when you book.

Used Python for EDA, SQL for deeper queries, and built a dashboard in Power BI.

---

## What I used

- Python (pandas, matplotlib, seaborn)
- SQL (SQLite + DBeaver)
- Power BI
- Git

---

## What I looked at

- Does flying further always mean paying more?
- Which airline is actually the most expensive?
- Is there any point booking early?
- How big is the gap between Economy and First?

---

## What I found

Class matters way more than distance. Correlation between distance and price 
is 0.64 — decent but not the whole story. Booking earlier barely helps (-0.32).

| Class | Avg Price |
|-------|-----------|
| Economy | $1,054 |
| Business | $1,940 |
| First | $3,049 |

Saudia is the priciest on average, Etihad the cheapest.
Most expensive single ticket: London → Mumbai, $8,853 First Class.

---

## Stack
```
data/                       source CSV
notebooks/eda_analysis.py   EDA script
sql/analysis_queries.sql    8 SQL queries
scripts/load_to_sqlite.py   loads CSV into SQLite
reports/                    charts and dashboard
```

---

## Dashboard

<img width="1160" height="654" alt="1pageATPA" src="https://github.com/user-attachments/assets/9ca90c4f-1c9a-4894-8c83-9f2ac547b412" />


---

## How to run
```bash
git clone https://github.com/amirb91-ux/airline-price-analysis.git
cd airline-price-analysis
pip install -r requirements.txt
python notebooks/eda_analysis.py
```
