import pandas as pd

data = pd.read_csv("Movie-Data.csv")


print(data.iloc[0:10,0:12])