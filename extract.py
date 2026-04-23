import pandas as pd
import requests
from pathlib import Path

url = "https://steamspy.com/api.php?request=all&page=1"

response = requests.get(url)
response.raise_for_status()
data = response.json()
df = pd.DataFrame(data)

folder_path = Path("data") / "raw" 
file_path = folder_path / "steamspy_data.csv"

df.to_csv(file_path, index=False)