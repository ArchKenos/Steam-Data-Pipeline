from extract import fetch_all_games
from transform import transform
from load import create_table

def pipeline():
    fetch_all_games(total_pages=0)
    transform()
    create_table()


if __name__ == "__main__":
    pipeline()
