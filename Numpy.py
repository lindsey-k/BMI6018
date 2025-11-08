#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np

#1. Import numpy as np and print the version number. (5 Points)
print("NumPy Version:", np.__version__)

 

 

#2. Create a 1D array of numbers from 0 to 9. Desired output:

#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])(10 Points)
#corefeatureofnumpy

 
array_1d = np.arange(10)
print("1D array:", array_1d)
 

#3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)
# Using NumPy function: np.genfromtxt() to read CSV data

 url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype='object')
print("Iris dataset loaded successfully. Shape:", iris.shape)

 

#4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)

 petal_width = iris[:, 3].astype(float)
position = np.argmax(petal_width > 1.0)
print("First occurrence of petal width > 1.0 is at index:", position)

 

#5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.

np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print("Original array:\n", a)

#Replace values greater than 30 → 30
#Replace values less than 10 → 10
a[a > 30] = 30
a[a < 10] = 10

print("Modified array:\n", a)
Input:

np.random.seed(100)
a = np.random.uniform(1,50, 20)

