import pandas as pd
""" Function to get the mean of Total cost & Function to recall just the Regions. """

data = pd.read_csv("100 Sales Records.csv")

print(data["Total Cost"].mean())

data = pd.read_csv("100 Sales Records.csv")

print(data[["Region"]])

