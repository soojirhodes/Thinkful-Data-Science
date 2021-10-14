#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
from scipy import stats
import math
import matplotlib.pyplot as plt

rfft = pd.read_csv("rfft.csv")


# In[2]:


rfft.info()
rfft.head()


# # 1. Is there a significant difference in the number of unique designs drawn by the same participants from measurement 2 to measurement 3?

# In[8]:


unique_meas_2 = rfft[rfft['Measurement'] == "Measurement 2 (2006-2008)"]
unique_meas_3 = rfft[rfft['Measurement'] == "Measurement 3 (2008-2012)"]

unique_meas_2.info()
unique_meas_3.info()


# In[14]:


# Pivot the data.

rfft_unique = rfft.pivot(index = "Casenr", columns = "Measurement", values = "Unique")
rfft_unique.head()


# In[16]:


rfft_unique['diff'] = rfft_unique['Measurement 3 (2008-2012)'] - rfft_unique['Measurement 2 (2006-2008)']

plt.hist(rfft_unique['diff'])

print(stats.describe(rfft_unique['diff']))


# In[17]:


stats.ttest_rel(rfft_unique['Measurement 3 (2008-2012)'], rfft_unique['Measurement 2 (2006-2008)'])


# The test statistic is greater than 1.96, and p-value is less than 0.05. Hence, we reject the null hypothesis, and conclude that there is a significant difference in the number of unique designs drawn by the same participants from measurement 2 to measurement 3.

# # 2. Is there a significant difference in the number of perseverative errors drawn by the same participants from measurement 2 to measurement 3?

# In[19]:


rfft_pers = rfft.pivot(index = "Casenr", columns = "Measurement", values = "Perseverative")

rfft_pers.head()


# In[21]:


rfft_pers['diff'] = rfft_pers['Measurement 3 (2008-2012)'] - rfft_pers['Measurement 2 (2006-2008)']
rfft_pers.head()

plt.hist(rfft_pers['diff'])

print(stats.describe(rfft_pers['diff']))


# In[27]:


# This did not pass the normality test, so we will use Wilcoxon signed-rank test.
print(stats.wilcoxon(rfft_pers['diff']))
#stats.wilcoxon((rfft_pers['Measurement 3 (2008-2012)'] - rfft_pers['Measurement 2 (2006-2008)']))

plt.hist(rfft_pers['Measurement 2 (2006-2008)'], alpha = 0.5)
plt.hist(rfft_pers['Measurement 3 (2008-2012)'], alpha = 0.5)


# ### Because the statistics is far greater than 1.96 and p value is less than 0.05, we reject the null hypothesis. There is a significant difference between perseverative erros from the same participants between the measurements.
