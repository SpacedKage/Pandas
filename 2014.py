import pandas as pd

data = pd.read_csv("Movie-Data.csv", index_col="Year")

"""
year_filter =(data["Year"]==2014)
year_filtered = data[year_filter]

print(year_filtered)
"""
df =pd.DataFrame(data)

print(df.loc[2014])