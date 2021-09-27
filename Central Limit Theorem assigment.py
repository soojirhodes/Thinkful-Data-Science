#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randint
from numpy import mean
from scipy import stats
from numpy.random import seed


# In[16]:


binom_results = []
for binom_num_trials in range(1,1000):
    binom_trials = np.random.binomial(7, 0.3, binom_num_trials)
    mean_of_binom_trials = binom_trials.mean()
    binom_results.append(mean_of_binom_trials)
    
binom_df = pd.DataFrame({'binom_trials': binom_results})

binom_df.plot()


# In[18]:


binom_means = [mean(np.random.binomial(7, 0.3,1000 )) for _ in range (1000)]

plt.hist(binom_means)
plt.show()


# In[19]:


poisson_results = []
for poisson_num_trials in range (1,1000):
    poisson_trials = np.random.poisson(7, poisson_num_trials)
    mean_of_poisson_trials = poisson_trials.mean()
    poisson_results.append(mean_of_poisson_trials)
    
poisson_df = pd.DataFrame({'poisson_trials': poisson_results})

poisson_df.plot()


# In[20]:


poisson_means = [mean(np.random.poisson(7, 1000)) for _ in range(1000)]

plt.hist(poisson_means)
plt.show()

