#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#UCI Breast Cancer dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"

#dataset does not have header, so I add simple names
cols = ["ID", "Diagnosis"] + [f"feature_{i}" for i in range(1, 31)]
df = pd.read_csv(url, header=None, names=cols)

#for clustering, I only use numeric features 
X = df.iloc[:, 2:]

print("Shape of X:", X.shape)
df.head()



# In[2]:


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[3]:


sse = []          
k_values = range(1, 11)   # k = 1 ~ 10

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    
    sse.append(kmeans.inertia_)

plt.plot(k_values, sse, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("SSE")
plt.title("Elbow Method for Breast Cancer Data")
plt.grid(True)
plt.show()


# In[4]:


#After looking at the elbow plot, I choose k=2


k_opt = 2
kmeans_final = KMeans(n_clusters=k_opt, random_state=42, n_init=10)
labels = kmeans_final.fit_predict(X_scaled)

print("Cluster counts:", pd.Series(labels).value_counts())


# In[5]:


x1 = X_scaled[:, 0]
x2 = X_scaled[:, 1]

centers = kmeans_final.cluster_centers_

plt.scatter(x1, x2, c=labels, alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')
plt.xlabel("feature_1 (scaled)")
plt.ylabel("feature_2 (scaled)")
plt.title(f"K-means clustering (k = {k_opt})")
plt.show()

#I used the Breast Cancer Wisconsin dataset (first link in the assignment).
#I standardized all numeric features and applied K-means clustering for k = 1–10.
#For each k I calculated the sum of squared error (SSE) and drew the elbow plot.
#The curve has a clear bend around k = 2, so I chose k = 2 as the optimal number of clusters.
#Finally, I plotted the clusters using the first two standardized features and marked the centroids.


# In[ ]:





# In[ ]:




