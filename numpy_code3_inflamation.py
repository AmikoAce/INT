#!/usr/bin/env python
# coding: utf-8

# # Example - Inflamation Data

# In[3]:


import numpy as np


# In[4]:


fname = "inflammation-01.csv"
data = np.loadtxt(fname, delimiter=',')
print(data)


# In[5]:


# properties of the data
print(type(data))
print(data.shape)
print("first value in data",data[0,0])
print("middle value in data:", data[30, 20])


# In[6]:


n,m = data.shape
data = data[:,10:(m-9)]
data


# In[12]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(data.mean(axis=0), label='avg')
plt.plot(data.max(axis=0), label='max')
plt.plot(data.min(axis=0), label='min')
plt.title('inflammation per day')
plt.legend()
plt.show()


# In[ ]:




