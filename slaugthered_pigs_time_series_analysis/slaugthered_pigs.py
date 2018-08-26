# Import packages
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Data import
df = pd.read_csv('monthly-total-number-of-pigs-sla.csv')
print(df.info())
df.columns = ['date', 'slaugthered_pigs']


#Convert month column to date and set as index
df.date = pd.to_datetime(df.date)
df.set_index('date', inplace=True)

#df.plot(figsize=(20,10), linewidth=5, fontsize=20)

#Get the trend, using rolling average to reduce seasonal influence
trend = df.rolling(12).mean()
trend.plot()

#Remove trend influence to anylize seasonality using first-order-difference
seas = df.diff()
seas.plot()

#Check for seasonal autocorrelation
pd.plotting.autocorrelation_plot(df[['slaugthered_pigs']])