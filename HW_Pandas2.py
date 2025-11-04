#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

#1
#creating  the series
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])

#calculating the distance
diff = p - q          

sq = diff ** 2         

s = sq.sum()           

dist = s ** 0.5           
dist



# In[2]:


#2

import pandas as pd
import numpy as np

#creating the dataframe
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df

#swap a&c
df = df[['c', 'b', 'a', 'd', 'e']]
df



# In[3]:


#3
import pandas as pd
import numpy as np

#creating dataframe
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df

#definging function and swap 2 columns
def swap_columns(df, col1, col2):
    cols = list(df.columns)
    i, j = cols.index(col1), cols.index(col2)
    cols[i], cols[j] = cols[j], cols[i]
    return df[cols]


df_swapped = swap_columns(df, 'a', 'c')
df_swapped


# In[4]:


#4
import pandas as pd
import numpy as np

#create data frame
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df

#displaying 4 decimals
pd.set_option('display.float_format', '{:.4f}'.format)

df



# In[5]:


#5
import pandas as pd
import numpy as np

#creating dataframe
df = pd.DataFrame(
    np.random.randint(1, 100, 40).reshape(10, -1),
    columns=list('pqrs'),
    index=list('abcdefghij')
)

#nearest row
def nearest_row(df):
    nearest_rows = []
    distances = []

    for i in range(len(df)):
        
        row_i = df.iloc[i].values
        
        dist = np.sqrt(((df - row_i) ** 2).sum(axis=1))
       
        dist.iloc[i] = np.inf

        
        nearest_idx = dist.idxmin()
        nearest_rows.append(nearest_idx)
        distances.append(dist.min())

    df['nearest_row'] = nearest_rows
    df['dist'] = distances
    return df

df_result = nearest_row(df)
df_result


# In[6]:


#6
import pandas as pd

#creating data
data = {
    'A': [45, 37, 0, 42, 50],
    'B': [38, 31, 1, 26, 90],
    'C': [10, 15, -10, 17, 100],
    'D': [60, 99, 15, 23, 56],
    'E': [76, 98, -0.03, 78, 90]
}

#creating dataframe
df = pd.DataFrame(data)


df.corr()


# In[ ]:




