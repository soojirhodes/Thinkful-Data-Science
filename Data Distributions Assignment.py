#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


gamma = np.random.gamma(3, 0.1, 100)
plt.hist(gamma, color = 'y')
plt.show()


# In[12]:


print(gamma.mean())
print(gamma.std())


# In[ ]:


plt.hist(gamma, color = 'y')
plt.axvline(gamma.mean(), color='r', linestyle='solid', linewidth=3)
plt.axvline(gamma.mean() + gamma.std(), color = 'r', linestyle = 'dashed', linewidth=3)
plt.axvline(gamma.mean() - gamma.std(), color='r', linestyle='dashed', linewidth=3)
plt.show()


# It shows above that the mean and the standard deviation are skewed to the left. 

# In[17]:


norm_rand_1 = np.random.normal(5, 0.5, 1000)
norm_rand_2 = np.random.normal(10, 1, 1000)

norm_rand_added = norm_rand_1 + norm_rand_2

plt.hist(norm_rand_added)
plt.show()


# In[18]:


plt.hist(norm_rand_added, color = 'c')
plt.axvline(norm_rand_added.mean(), color='g', linestyle='solid', linewidth=1)
plt.axvline(norm_rand_added.mean() - norm_rand_added.std(), color = 'g', linestyle='dotted', linewidth=1)
plt.axvline(norm_rand_added.mean() + norm_rand_added.std(), color='g', linestyle='dotted', linewidth=1)

plt.show()

