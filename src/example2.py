import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting._matplotlib import scatter_matrix as sm

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

df.hist(sharex=False, sharey=False, xlabelsize=15, ylabelsize=15, color="orange", figsize=(15,15))
plt.suptitle("histograms", y=1.00, fontweight="bold", fontsize=40)
plt.savefig("histograms.png") # or plt.show()

df.plot(kind="density", subplots=True, layout=(7,2), sharex=False, fontsize=16, figsize=(15,15))
plt.suptitle("density", y=1.00, fontweight="bold", fontsize=40)
plt.savefig("probabilityDensity.png")

df.plot(kind="box", subplots=False, layout=(4,4), sharex=False, sharey=False, fontsize=16, figsize=(10,10))
plt.suptitle("boxAndWhisker", y=1.00, fontweight="bold", fontsize=40)
plt.savefig("boxAndWhisker.png")

axes=(sm(df, figsize=(15,15)))
plt.suptitle("scatter matric", y=1.00, fontweight="bold", fontsize=30)
plt.rcParams["axes.labelsize"]=15
[plt.setp(item.yaxis.get_majorticklabels(),"size",15) for item in axes.ravel()]
[plt.setp(item.xaxis.get_majorticklabels(),"size",15) for item in axes.ravel()]
plt.savefig("scatter matric.png")

# todo
plt.figure(figsize=(11,11))
plt.style.use("default")
sns.heatmap(df.corr(), annot=true)
