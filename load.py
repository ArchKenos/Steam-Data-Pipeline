from pathlib import Path
import duckdb

DB_PATH = Path('data') / 'steam.db'
clean_data = Path('data/clean') / 'steamspy_cleaned.parquet'

def create_table():
    with duckdb.connect (DB_PATH) as con:
        con.execute('''CREATE OR REPLACE TABLE games(
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
                        owners_min         INT,
                        owners_max         INT
                        )
                        ''')
        con.execute("INSERT INTO games" \
        "            SELECT * " \
        f"            FROM read_parquet('{clean_data}')")
        con.table('games').show(max_width= 200)

if __name__ == '__main__':
    create_table()