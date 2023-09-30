#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[12]:


data = pd.read_csv('output2.csv')


# In[13]:


data.head(50)


# In[6]:


data['name'].nunique()


# In[7]:


data['name'].value_counts()


# In[16]:


data['country'] = data['name'].str.split(',').str[-1].str.split('-').str[0].str.strip()


# In[17]:


data.head()


# In[19]:


data['country'].unique()


# In[21]:


data.to_csv('tesla_superchargers_eu.csv', index=False)


# In[ ]:




