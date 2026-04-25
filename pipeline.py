import logging
from extract import fetch_all_games
from transform import transform
from load import load_into_schema

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def pipeline():
    fetch_all_games(total_pages=3)
    transform()
    load_into_schema()


if __name__ == "__main__":
    pipeline()
