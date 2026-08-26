# 🎮 Steam Data Pipeline

ETL pipeline that collects Steam game data from the SteamSpy API,
cleans and models it, and loads it into DuckDB for analytical queries.

## 🏗️ Architecture

<pre>SteamSpy API ➡️ [extract.py] ➡️ data/raw/ (JSON)                           
                                     ⬇️  
                               [transform.py] ➡️ data/clean/ (Parquet)  
                                                   ⬇️  
                                                 [load.py] ➡️ steam.db (DuckDB)
</pre>
🛠️ Orchestrated by pipeline.py

## 💻 Tech Stack

| Tool | Role |
|---|---|
| 🐍 Python + Requests | API ingestion |
| 🐼 Pandas | Data cleaning and transformation |
| 🗜️ Parquet + PyArrow | Typed intermediate storage |
| 🦆 DuckDB | Analytical database (OLAP) |
| ⚡ uv | Dependency management |

## 🚀 How to Run

```
git clone https://github.com/ArchKenos/Steam-Data-Pipeline  
cd Steam-Data-Pipeline  
uv sync  
uv run pipeline.py  
```
## 📂 Project Structure

- extract.py    ➡️ fetches raw JSON pages from SteamSpy API  
- transform.py  ➡️ cleans data and outputs Parquet  
- load.py       ➡️ creates DuckDB schema and loads Parquet  
- pipeline.py   ➡️ orchestrates the full ETL run  
- data/raw/     📁 raw API responses (not versioned)  
- data/clean/   📁 cleaned Parquet files (not versioned)
- data/steam.db 🦆 DuckDB file for SQL-base analysis (not versioned)

## 🧠 Design Decisions

- DuckDB over PostgreSQL: No server setup required — runs entirely local. 🦆
- Parquet as intermediate format: preserves column types, 
  compresses better than CSV. 📈
- Raw JSON preserved before transformation: original API
  response stored following data lake principles. 📥
- owners field split into owners_min and owners_max: SteamSpy
  returns ownership as a range string ("200,000 .. 500,000"). 🔢

## ⚠️ Known Limitations

- **Data Accuracy**: Owners data is a SteamSpy estimate — Steam privacy policy limits accuracy
- **Rate Limiting**: The pipeline is configured to extract 3 pages (~3,000 games) by default to demonstrate functionality within 2-3 minutes.
  While the script is fully capable of extracting the entire 90,000+game catalog, the SteamSpy API enforces a **1-minute delay** per page ⏳,
  resulting in a total ingestion window of approximately 90 minutes for the full dataset.
- **Manual Trigger**: No pipeline scheduling — runs manually

📊 BI
<img width="1302" height="730" alt="image" src="https://github.com/user-attachments/assets/fc00acc9-c4c9-4b85-9ed9-c5463a4b31b9" />


