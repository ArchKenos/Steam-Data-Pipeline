import json
import time
import requests
from pathlib import Path

RAW_DIR = Path("data") / "raw" 
PAGE_DELAY = 60 #Time to refresh page requisition

def fetch_page(page):

    url = f"https://steamspy.com/api.php?request=all&page={page}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_raw_data(data, page):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    file_path = RAW_DIR / f"steamspy_page{page}.json"
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_all_games(total_pages: int = 3):
    for page in range(0, total_pages):
        data = fetch_page(page)
        save_raw_data(data, page)
        if (page < total_pages - 1):
            time.sleep(PAGE_DELAY)

if __name__ == "__main__":
    fetch_all_games()