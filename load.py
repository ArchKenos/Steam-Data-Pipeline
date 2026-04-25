from pathlib import Path
import duckdb

DB_PATH = Path('data') / 'steam.db'

clean_data = Path('data/clean') / 'steamspy_cleaned.parquet'

with duckdb.connect (DB_PATH) as con:
    con.execute('''CREATE TABLE IF NOT EXISTS games(
                     appid              INT,
                     name               VARCHAR(50),
                     developer          VARCHAR(50),
                     publisher          VARCHAR(50),
                     positive           INT,
                     negative           INT,
                     price              INT,
                     initialprice       INT,
                     discount           INT,
                     ccu                INT,
                     owners_min         VARCHAR(15),
                     owners_max         VARCHAR(15)
                     )
                     ''')
    con.execute("INSERT INTO games" \
    "            SELECT * " \
    f"            FROM read_parquet('{clean_data}')")
    con.table('games').show(max_width= 200)
