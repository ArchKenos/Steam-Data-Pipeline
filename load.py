from pathlib import Path
import duckdb

DB_PATH = Path('data') / 'steam.db'
clean_data = Path('data/clean') / 'steamspy_cleaned.parquet'

def insert_into_table(con):
    con.execute("INSERT INTO games" \
        "            SELECT * " \
        f"            FROM read_parquet('{clean_data}')")
    
def create_schema(con):
        con.execute('''CREATE OR REPLACE TABLE games(
                        appid              INT,
                        name               VARCHAR(200),
                        developer          VARCHAR(250),
                        publisher          VARCHAR(200),
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
        
def load_into_schema():
    with duckdb.connect (DB_PATH) as con:
        create_schema(con)
        insert_into_table(con)
        con.table("games").show(max_width= 200)

if __name__ == '__main__':
    load_into_schema()