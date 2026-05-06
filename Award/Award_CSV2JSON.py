import pandas as pd
import json

df = pd.read_excel("第十届教育部人文社科奖.xlsx")

data = df.fillna("").to_dict(orient="records")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)