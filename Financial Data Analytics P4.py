#!/usr/bin/env python
# coding: utf-8

# ### Importing necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Reading and formatting the data for analysis

# In[2]:


financial_data = pd.read_csv("Financial Analytics data.csv")
financial_data['Sales Qtr - Crore'] = financial_data['Sales Qtr - Crore'].combine_first(financial_data['Unnamed: 4'])
financial_data.drop(["Unnamed: 4","S.No."],axis=1,inplace=True)
financial_data = financial_data.dropna()
financial_data.head()


# ### Checking for null values

# In[3]:


financial_data.isnull().sum()


# In[4]:


financial_data.describe()


# In[5]:


financial_data.info()


# ### The biggest comapanies Market Cap and Sales Qtr wise

# In[6]:


financial_data.sort_values("Mar Cap - Crore",ascending=False)


# In[7]:


financial_data.sort_values("Sales Qtr - Crore",ascending=False)


# In[8]:


plt.scatter(financial_data["Mar Cap - Crore"],financial_data["Sales Qtr - Crore"])
plt.xlabel("Mar Cap - Crore")
plt.ylabel("Sales Qtr - Crore")
plt.title("Market Cap Vs Sales")
plt.show()

