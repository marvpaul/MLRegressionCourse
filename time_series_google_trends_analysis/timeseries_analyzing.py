# Import packages
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Data import
df = pd.read_csv('multiTimeline.csv', skiprows=1)

#Wrangle / reformat data

#Rename columns, get rid of whitespaces
df.columns = ['month', 'diet', 'gym', 'finance']

#Convert month column to date and set as index
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)

#EDA / Exploratory data analysis / Visualize data
#Build in pandas plotting tool with some custom params
#df.plot(figsize=(20,10), linewidth=5, fontsize=20)
#plt.xlabel('Year', fontsize=20)

def analyze_trend(df, column_name):
    '''
    This method is using rolling average with window size of 12 to remove
    potential seasonality from df
    :param df:
    :param column_name:
    :return:
    '''
    column = df[[column_name]]
    return column.rolling(12).mean()


#Trend of gym
df[['gym']].plot()
analyze_trend(df, 'gym').plot()

def compare_two_trends(trend1, trend2):
    df_rm = pd.concat([trend1, trend2], axis=1)
    df_rm.plot(figsize=(20,10), linewidth=5, fontsize=20)
    plt.xlabel('Year', fontsize=20)


compare_two_trends(analyze_trend(df, 'gym'), analyze_trend(df, 'diet'))

