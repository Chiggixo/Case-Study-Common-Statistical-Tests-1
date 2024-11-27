#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency


# In[8]:


data = pd.read_csv('Employee-Attrition.csv')


# In[10]:


data.head()


# In[12]:


data = pd.read_csv('Employee-Performance-Data.csv')


# In[13]:


data.head()


# In[14]:


dept_a = data[data['Department'] == 'A']['Performance_Score']
dept_b = data[data['Department'] == 'B']['Performance_Score']
t_stat, p_value = ttest_ind(dept_a, dept_b)
print(f"T-test: t-statistic = {t_stat}, p-value = {p_value}")


# In[16]:


contingency_table = pd.crosstab(data['Department'], data['Promotions'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square Test: chi2 = {chi2}, p-value = {p}")


# In[ ]:




