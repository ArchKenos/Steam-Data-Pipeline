from extract import fetch_all_games
from transform import transform

def pipeline():
    fetch_all_games(total_pages=10)
    transform()


if __name__ == "__main__":
    pipeline()
