import pandas as pd

MovieData = pd.read_csv("Movie-Data.csv", index_col="Director")



print(MovieData.loc[["Ridley Scott", "Tom Ford"]])


