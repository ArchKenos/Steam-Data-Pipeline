import logging
from pathlib import Path
import duckdb

logger = logging.getLogger(__name__)

DB_PATH = Path('data') / 'steam.db'
clean_data = Path('data/clean') / 'steamspy_cleaned.parquet'

def insert_into_table(con):
    con.execute("INSERT INTO games" \
        "            SELECT * " \
        f"            FROM read_parquet('{clean_data}')")
    logger.info("Data inserted into 'games' table ")
    
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
        logger.info("Table 'games' created")
        
        
def load_into_schema():
    with duckdb.connect (DB_PATH) as con:
        create_schema(con)
        insert_into_table(con)

if __name__ == '__main__':
    load_into_schema()