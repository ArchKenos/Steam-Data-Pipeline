import pandas as pd
from pathlib import Path


RAW_DIR = Path("data") / "raw" 
raw_file = RAW_DIR / "steamspy_page0.json"
CLEAN_DIR = Path("data") / "clean" 
clean_file = CLEAN_DIR / 'steamspy_page0.parquet'



df = pd.read_json(raw_file, orient='index')
df = df.reset_index(drop=True)
df = df.drop(columns=['score_rank', 'userscore', 'average_forever', 'average_2weeks', 'median_forever', 'median_2weeks'])


clean_file.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(clean_file)


