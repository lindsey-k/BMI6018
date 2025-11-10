#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


#Data Loading

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/arrhythmia.data"
cols = [f"feature_{i}" for i in range(1, 280)] + ["class"]   
df = pd.read_csv(url, header=None, names=cols, na_values="?")

print("shape:", df.shape)
print(df.head(), "\n")


#Melt,wide to long

melted = pd.melt(
    df.head(10),                     
    id_vars=["class"],
    value_vars=["feature_1", "feature_2", "feature_3", "feature_4", "feature_5"],
    var_name="feature_name",
    value_name="value"
)
print("Melt result:")
print(melted.head(), "\n")


#Pivot, long to wide
#make it column

pivoted = melted.pivot(
    index="class",
    columns="feature_name",
    values="value"
)
print("Pivot result:")
print(pivoted.head(), "\n")


#Aggregation:summary by class

agg = (
    df.groupby("class")
      .agg(
          feature1_mean=("feature_1", "mean"),
          feature1_median=("feature_1", "median"),
          feature2_mean=("feature_2", "mean"),
          feature3_mean=("feature_3", "mean"),
          count_rows=("feature_1", "count")   #nonmissing count
      )
      .reset_index()
)
print("Aggregation by class:")
print(agg.head(), "\n")


#Iteration: counting

missing_rows = 0
for _, r in df.iterrows():
    if r.isna().any():
        missing_rows += 1

print("Rows with >=1 missing value:", missing_rows, "\n")



#Groupby: mean by class

grouped_mean = (
    df.groupby("class")[["feature_1", "feature_2", "feature_3"]]
      .mean()
      .reset_index()
      .rename(columns={
          "feature_1": "feature1_mean",
          "feature_2": "feature2_mean",
          "feature_3": "feature3_mean"
      })
)
print("Groupby mean by class:")
print(grouped_mean.head())


# In[ ]:




