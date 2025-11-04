#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

flights_data = pd.read_csv('BMI6018/flights.csv')
weather_data = pd.read_csv('BMI6018/weather.csv')

flights_data.head()


# In[2]:


#1
q_1 = len(flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')])
q_1


# In[3]:


#Q2
q_2 = flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique()
q_2


# In[4]:


#Q3
q_3 = flights_data[flights_data['dest'] == 'SLC']['arr_delay'].mean()
q_3


# In[5]:


#4
q_4 = len(flights_data[(flights_data['origin'] == 'JFK') & (flights_data['arr_delay'] >= 30)])
q_4


# In[6]:


#5
q_5 = flights_data[flights_data['dest'] == 'SLC']['dep_delay'].mean()
q_5


# In[7]:


#Q6
flights_data['date'] = flights_data[['year', 'month', 'day']].astype(str).agg('/'.join, axis=1)

avg_arr_delay_by_date = flights_data.groupby('date')['arr_delay'].mean()

q_6 = avg_arr_delay_by_date.idxmax(), avg_arr_delay_by_date.max()
q_6


# In[8]:


#Q7
tmp = flights_data[flights_data['air_time'] > 0].copy()   # 0/NaN 제거
tmp['speed'] = tmp['distance'] / (tmp['air_time'] / 60)   # mph

q_7 = (tmp[tmp['origin'].isin(['JFK','LGA'])]
       .loc[:, ['tailnum','origin','dest','distance','air_time','speed']]
       .sort_values('speed', ascending=False)
       .head(1))

q_7


# In[9]:


#Q8

weather_data.isnull().sum()     

weather_data = weather_data.fillna(0)   
weather_data.isnull().sum()     



# In[10]:


import numpy as np


weather_data_np = weather_data.to_numpy()


cols = list(weather_data.columns)
month_idx = cols.index('month')
humid_idx = cols.index('humid')

#Q9
q_9 = int(np.sum(weather_data_np[:, month_idx] == 2))
q_9


# In[11]:


#10
mask_feb = (weather_data_np[:, month_idx] == 2)
humid_feb = weather_data_np[mask_feb, humid_idx].astype(float)

q_10 = float(np.mean(humid_feb))
q_10


# In[12]:


#Q11
q_11 = float(np.std(humid_feb))
q_11


# In[ ]:




