import numpy as np
import pandas as pd

pd.set_option("display.max_rows",500)
pd.set_option("display.max_columns",500)
pd.set_option("display.width",1000)


filename="../data/forestfires.csv"
names=["X","Y","month","day","FFMC","DMC","DC","ISI","TEMP","RH","wind", "rain", "area"]
df= pd.read_csv(filename,names=names)

print(pd.isnull(df).sum())
print(df.shape)
print(df.dtypes)
print(df.head())
print(df.describe())
print(df.corr(method="pearson"))

df.month.replace(("jan","feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"),(1,2,3,4,5,6,7,8,9,10,11,12),inplace=True)
df.day.replace(("mon","tue","wed", "thu","fri","sat","sun"),(1,2,3,4,5,6,7),inplace=True)

print(df.head())
