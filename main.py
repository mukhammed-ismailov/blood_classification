import pandas as pd

from  config import *

data = pd.read_csv(csv_file)

# show data information
print(data.head())
print(data.info())
print(data.describe())

