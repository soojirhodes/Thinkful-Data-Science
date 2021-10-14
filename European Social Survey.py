#!/usr/bin/env python
# coding: utf-8

# * Did people become less trusting from 2012 to 2014?
# * Did people become happier from 2012 to 2014?
# * Pick three or four of the countries in the sample and compare how often people met socially in 2014. Are there differences, and if so, which countries stand out?
# * Pick three or four of the countries in the sample and compare how often people took part in social activities, relative to others their age, in 2014. Are there differences, and if so, which countries stand out?

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
from scipy import stats
import math
import matplotlib.pyplot as plt

survey = pd.read_csv("ess_combined_2012_2014.csv")

survey.info()
survey.head()

yr_2012 = survey[survey["year"] == 6]
yr_2014 = survey[survey["year"] == 7]


# # 1. Did people become less trusting from 2012 to 2014?

# In[8]:


# Visualization check.
plt.hist(yr_2012['ppltrst'], alpha = .5, label = "2012 trust")
plt.hist(yr_2014['ppltrst'], alpha = .5, label = "2014 trust")
plt.legend(loc = "upper left")
plt.show()

print(stats.describe(yr_2012['ppltrst']))
print(stats.describe(yr_2014['ppltrst']))


# In[3]:


# It does seem to be normal, with the skewness and kurtosis both fall within 3 and -3.
# Shapiro-Wilk for another normality check.
print(stats.shapiro(yr_2012['ppltrst']))
print(stats.shapiro(yr_2014['ppltrst']))


# In[4]:


# Since it is normally distributed, we will conduct a t-test.
stats.ttest_ind(yr_2012['ppltrst'],
               yr_2014['ppltrst'])


# ### The t-test result is not greater than 1.96, and p-value is greater than 0.05 - hence, we cannot reject the null. There is no significant difference in trust between 2012 and 2014.

# # 2. Did people become happier from 2012 to 2014?

# In[10]:


# Visualization check.
plt.hist(yr_2012['happy'], alpha = 0.5, label = "2012 happiness")
plt.hist(yr_2014['happy'], alpha = 0.5, label = "2014 happiness")
plt.legend(loc ="upper left")
plt.show()

print(stats.describe(yr_2012['happy']))
print(stats.describe(yr_2014['happy']))


# In[14]:


# Visualization shows not normally distributed.
# Kruskal-Wallis test.

print(stats.kruskal(yr_2012['happy'],yr_2014['happy']))


# ### P-value is very close to 0.05. Also, because of the visual inspeciton, it is understood that we failed to reject the null hypothesis. 

# # 3. Pick three or four of the countries in the sample and compare how often people met socially in 2014. Are there differences, and if so, which countries stand out?

# In[26]:


# How many unique countries are there?
survey['cntry'].unique()


# In[33]:


# Now we will create separate dataset for each country.
Germany = survey[survey["cntry"] == "DE"]
Spain = survey[survey["cntry"] == "ES"]
Norway = survey[survey["cntry"] == "NO"]
Sweden = survey[survey["cntry"] == "SE"]

# Germany only has 27 samples, so we will only use Spain, Norway, and Sweden.


# In[37]:


filter_list = ['ES', 'NO', 'SE']
three_country = survey[survey['cntry'].isin(filter_list)]

three_country['cntry'].unique()

three_country['sclmeet'].hist(by = three_country['cntry'])


# In[38]:


# These are sparser samples of original data, so nothing will be perfectly "normal".
# Let's run a Kruskal Wallis test.

stats.kruskal(
    three_country.loc[three_country['cntry'] == 'ES', ['sclmeet']],
    three_country.loc[three_country['cntry'] == 'NO', ['sclmeet']],
    three_country.loc[three_country['cntry'] == 'SE', ['sclmeet']])


# p-value is less than 0.05, and statistics is high. One or more of them has a significantly different median.

# In[40]:


three_country.boxplot('sclmeet', by='cntry', figsize=(10,6))


# ### Sweden has a different median than the other countries.

# # 4. Pick three or four of the countries in the sample and compare how often people took part in social activities, relative to others their age, in 2014. Are there differences, and if so, which countries stand out?

# In[41]:


three_country['sclact'].hist(by = three_country['cntry'])


# In[43]:


# These look a little more normal as they look more symmetrical.
# These call for one-way ANOVA.

stats.f_oneway(
    three_country.loc[three_country['cntry'] == 'ES', ['sclact']],
    three_country.loc[three_country['cntry'] == 'NO', ['sclact']],
    three_country.loc[three_country['cntry'] == 'SE', ['sclact']])


# In[46]:


# Looks significant.
# LEt's try Tukey's HSD.
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog = three_country['sclact'],
                         groups = three_country['cntry'],
                         alpha = 0.05)

tukey.summary()


# ### We can reject the null hypothesis for Spain. In other words, relative to their age, people in spain took less social activities than other countries.
