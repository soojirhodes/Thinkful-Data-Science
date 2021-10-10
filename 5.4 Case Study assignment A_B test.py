#!/usr/bin/env python
# coding: utf-8

# # Instructions
# 1. Check for adequate sample sizes.
# 1. Check for changes over time in results.
# 1. Formally test for a significant difference in conversions between treatment and control groups.

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats

exp_data = pd.read_csv('ab_edited.csv')


# In[13]:


exp_data.info()
exp_data.head(10)


# In[27]:


# Let's convert the timestamp to date.
exp_data['date'] = pd.DatetimeIndex(experiment_data['timestamp']).date

#exp_data.head(10)
print(exp_data.date.unique())


# ## 1. Check for adequate sample sizes.

# In[28]:


print('treatment sample size:', len(exp_data[exp_data.group == 'treatment']))
print('control sample size:', len(exp_data[exp_data.group == 'control']))
print('test proportion:', exp_data.converted.mean())

print('treatment signup rate:', exp_data[exp_data.group == 'treatment'].converted.mean())
print('control signup rate:', exp_data[exp_data.group == 'control'].converted.mean())


# ## 2. Check for changes over time in results.

# In[20]:


fig = exp_data[exp_data.group == 'treatment'][
    ['date', 'converted']].groupby('date').mean().plot()
exp_data[exp_data.group == 'control'][
    ['date', 'converted']].groupby('date').mean().plot(ax=fig)
plt.legend(['treatment', 'control'])
plt.title('Comparing Signup Rates by Treatment Date')
plt.show()


# ## 3. Formally test for a significant difference in conversions between treatment and control groups.

# In[25]:


stats.ttest_ind(exp_data[exp_data.group == 'treatment'].converted,
               exp_data[exp_data.group == 'control'].converted)


# In[26]:


print('T-Test Results by Date')

for dates in exp_data.date.unique():
    dated_data = exp_data[exp_data.date == dates]
    print(stats.ttest_ind(dated_data[dated_data.group == 'treatment'].converted,
                         dated_data[dated_data.group == 'control'].converted))


# The answer is not significant!
