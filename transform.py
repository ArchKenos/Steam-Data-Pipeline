import pandas as pd
from pathlib import Path
import glob

RAW_DIR = Path("data") / "raw" 
CLEAN_DIR = Path("data") / "clean" 

#owners comes from API as ("10,000 .. 50,000")
#commas must be removed and the range defined
def  separate_owners_data(df):

    df["owners"] = df["owners"].str.replace(',','')
    owner_separation = df["owners"].str.split(" .. ",n=1, expand=True)
    df["owners_min"] = owner_separation[0]
    df["owners_max"] = owner_separation[1]
    df = df.drop(columns = "owners")
    return df

def read_raw_data():
    data_frame = []
    raw_pages = len(glob.glob('data/raw/*'))

    for page in range (0, raw_pages):
        raw_file = RAW_DIR / f"steamspy_page{page}.json"

        df = pd.read_json(raw_file, orient='index')
        df = df.reset_index(drop=True)
        df = separate_owners_data(df)
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
    print(df.head())
if __name__ == '__main__':
    transform()


