import pandas as pd
import requests

url = "https://steamspy.com/api.php?request=all&page=1"

response = requests.get(url)
response.raise_for_status()
data = response.json()
df = pd.DataFrame(data)
