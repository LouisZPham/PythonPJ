import csv
import pandas as pd
data = {"Name": ["TIN", "LOUIS", "REMY"],
        "Age": [23, 21, 28]}
data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())

data = pd.read_csv("age_data.csv")
print(data.head())