"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""

# TODO Import the necessary libraries
import pandas as pd
import numpy as np
import io
from pandas.tseries.offsets import DateOffset
import datetime
from google.colab import files
uploaded = files.upload()

# TODO Import the dataset 

path = r'./data/weather_dataset.data'

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
df = pd.read_csv(io.StringIO(uploaded['weather_dataset.csv'].decode('utf-8')), sep=' ')

print("The count of NANs:",'\n', df.shape[0] - df.notnull().sum())

df = df.dropna()
#replace the first 3 columns by a proper datetime index ---> soon

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them

df = df.replace(to_replace='None', value=np.nan).dropna()
df = df.replace(to_replace='NONE', value=np.nan).dropna()
df = df.replace(to_replace='nodata', value=np.nan).dropna()
df = df.replace(to_replace='1.0k', value=np.nan).dropna()
df = df.replace(to_replace='-123*None', value=np.nan).dropna()
df = df.replace(to_replace='9999999999999999', value=np.nan).dropna()
df = df.replace(to_replace=str(min(df['loc9'].astype(float))), value=np.nan).dropna()
df = df.replace(to_replace=1.000000e-17, value=np.nan).dropna()

# TODO Write a function in order to fix date (this relate only to the year info) and apply it

df['Yr'] = df['Yr'].astype(int) + 1900
df['Mo'] = df['Mo'].astype(int)
df['Dy'] = df['Dy'].astype(int)

df['dateInt'] = df['Yr'].astype(str) + df['Mo'].astype(str) + df['Dy'].astype(str)
df['Date'] = pd.to_datetime(df['dateInt'], format='%Y%m%d')

df = df.drop(['Yr', 'Mo', 'Dy', 'dateInt'], axis=1)

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

df = df.set_index(df['Date'])
df.index.astype("datetime64[ns]")

df = df.drop(['Date'], axis = 1)

# TODO Compute how many values are missing for each location over the entire record

print("The count of NANs:",'\n', df.shape[0] - df.notnull().sum())
'''
loc1     11
loc2      8
loc3      8
loc4     10
loc5      7
loc6      5
loc7      8
loc8      7
loc9      9
loc10     6
loc11     5
loc12     9
'''
# TODO Compute how many non-missing values there are in total

print("The number of rows after dropna:", df.shape[0]) #6539

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
for element in df.columns:
  df[f'{element}'] = df[f'{element}'].astype(float)
  
print("Mean over all the locations and all the times", df.mean().mean())

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

def min_func(df):
  a = []
  for element in df.columns:
    a.append(df[f'{element}'].astype(float).min())
  return a

def max_func(df):
  b = []
  for element in df.columns:
    b.append(df[f'{element}'].astype(float).max())
  return b

def mean_func(df):
  c = []
  for element in df.columns:
    c.append(df[f'{element}'].astype(float).mean())
  return c

def std_func(df):
  d = []
  for element in df.columns:
    d.append(df[f'{element}'].astype(float).std())
  return d

loc_stats = pd.DataFrame({'min': min_func(df),
                   'max': max_func(df),
                   'mean': mean_func(df),
                   'std': std_func(df)})

display(loc_stats.set_index(df.columns))

# TODO Find the average windspeed in January for each location

jan = df[df.index.month == 1]
print ("January:")
print (jan.mean())

# TODO Downsample the record to a yearly frequency for each location

display(df.resample('Y').mean())

# TODO Downsample the record to a monthly frequency for each location

display(df.resample('M').mean())

# TODO Downsample the record to a weekly frequency for each location

week_data = df.resample('W').mean()

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

week_data_mean = df.resample('W').mean()
first_weeks_mean = week_data_mean.head(21)
display(first_weeks_mean)

week_data_min = df.resample('W').min()
first_weeks_min = week_data_min.head(21)
display(first_weeks_min)

week_data_max = df.resample('W').max()
first_weeks_max = week_data_max.head(21)
display(first_weeks_max)

week_data_std = df.resample('W').std()
first_weeks_std = week_data_std.head(21)
display(first_weeks_std)
