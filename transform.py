import pandas as pd
from pathlib import Path
import glob

RAW_DIR = Path("data") / "raw" 
CLEAN_DIR = Path("data") / "clean" 

def read_raw_data():
    data_frame = []
    raw_pages = len(glob.glob('data/raw/*'))

    for page in range (0, raw_pages):
        raw_file = RAW_DIR / f"steamspy_page{page}.json"

        df = pd.read_json(raw_file, orient='index')
        df = df.reset_index(drop=True)
        df = df.drop(columns=['score_rank', 'userscore',
                            'average_forever', 'average_2weeks', 
                            'median_forever', 'median_2weeks'])
        data_frame.append(df)
    df_save = pd.concat(data_frame)

    return df_save

def save_clean_data(df):

    clean_file = CLEAN_DIR / 'steamspy_cleaned.parquet'
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(clean_file, index=False)

def transform():
    df = read_raw_data()
    save_clean_data(df)

if __name__ == '__main__':
    transform()


