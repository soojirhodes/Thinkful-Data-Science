#!/usr/bin/env python
# coding: utf-8

# For this assignment, you'll use a real-life dataset of housing prices, as published in the [Journal of Applied Econometrics](http://qed.econ.queensu.ca/jae/1996-v11.6/anglin-gencay/). [Download the data here.](https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/homeprices.applied.econ.csv)
# 
# Explore the following questions. Include a hypothesis, test assumptions, and provide valid findings from the data.
# 1. Do homes with air conditioning have a higher sales price than homes without air conditioning?
# 1. Do homes with a full basement have a higher sales price than homes without a full basement?
# 
# As you are conducting the analysis, consider what other variables may be accounting for any significant differences that you find.
# 
# When you are finished, compare your Notebook to [this one](https://colab.research.google.com/drive/1IDnrmj41g_oXGStAYVZ9qhKijC-7_3CX).

# In[1]:


#First, set the environment.
import math
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

homeprices = pd.read_csv("https://tf-assets-prod.s3.amazonaws.com/tf-curric/data-science/homeprices.applied.econ.csv")


# In[2]:


# Get to know the data a bit.
homeprices.info()
homeprices.head()


# For the first question:
# * $H_o$: Homes with air conditioning has equal sales price as homes without air conditioning.
# * $H_a$: Homes with air conditioning does not equal sales price as homes without air conditioning.
# 
# Assumptions of the t-test:
# 1. The test variable, which are sales prices, are continuous.
# 1. There is no relationship between homes with air conditioning and homes without air conditioning.
# 1. The sample is drawn at random from the population.
# 1. We will check if the variable samples and population are approximatly normally distributed by checking kurtosis and skewness.
# 1. We will check if the sample is reasonably large enough to be representative of the population.
# 1. The variances are approximately equal in both the sample and population.

# In[3]:


# Split up the dataset for the first question.
airco_yes = homeprices[(homeprices['airco'] == 'yes')]
airco_yes.info()
airco_no = homeprices[(homeprices['airco'] =='no')]
airco_no.info()


# This output validates that the samples are reasonably large enough to be representative of the population, with more than 30 in each set.

# In[4]:


# Before running the t-test, check whether the samples are normally distributed.
plt.hist(airco_yes['price'], alpha = .5, label = "airco yes")
plt.hist(airco_no['price'], alpha = .5, label = "airco no")
plt.legend(loc = "upper right")
plt.show()

print(stats.describe(airco_yes['price']))
print(stats.describe(airco_no['price']))


# This output confirms that the variable samples and population are approximatly normally distributed, with skewness within -3 and 3, and kurtosis between -8 and 8.

# In[5]:


stats.ttest_ind(airco_yes['price'], airco_no['price'])


# This output validates that we can reject the null hypothesis:
# 1. The test statistics is greater than 1.96.
# 2. The p-value is less than 0.05.

# In[6]:


# Now, calculate the confidence interval for 95%.
def get_95_ci(array_1, array_2):
    sample_1_n = array_1.shape[0]
    sample_2_n = array_2.shape[0]
    sample_1_mean = array_1.mean()
    sample_2_mean = array_2.mean()
    sample_1_var = array_1.var()
    sample_2_var = array_2.var()
    mean_difference = sample_2_mean - sample_1_mean
    std_err_difference = math.sqrt((sample_1_var/sample_1_n) + (sample_2_var/sample_2_n))
    margin_of_error = 1.96 * std_err_difference
    ci_lower = mean_difference - margin_of_error
    ci_upper = mean_difference + margin_of_error
    return("The difference in means at the 95% confidence interval (two-tail) is between " + str(ci_lower) + " and " + str(ci_upper) + ".")

get_95_ci(airco_yes['price'], airco_no['price'])


# With 95% confidence, houses with air conditioning sells between `$`30,758.99 and `$`21,233.38 more than houses without air conditioning.
# 
# Now, let's move on to the second problem set. 
# 
# For the second question:
# * $H_o$: Homes with full basement has equal sales price as homes without full basement.
# * $H_a$: Homes with full basement does not equal sales price as homes without full basement
# 
# The same assumption applies here.

# In[7]:


# Set the environment for the second question.
fullbase_yes = homeprices[(homeprices['fullbase'] == 'yes')]
fullbase_yes.info()

fullbase_no = homeprices[(homeprices['fullbase'] == 'no')]
fullbase_no.info()


# This output validates that the samples are reasonably large enough to be representative of the population, with more than 30 in each set.

# In[8]:


# Are the samples normally distributed?
plt.hist(fullbase_yes['price'], alpha = .5, label = "fullbase yes")
plt.hist(fullbase_no['price'], alpha = .5, label = "fullbase no")
plt.legend(loc = "upper right")
plt. show()

print(stats.describe(fullbase_yes['price']))
print(stats.describe(fullbase_no['price']))


# This output confirms that the variable samples and population are approximatly normally distributed, with skewness within -3 and 3, and kurtosis between -8 and 8.

# In[9]:


stats.ttest_ind(fullbase_yes['price'], fullbase_no['price'])


# This output validates that we can reject the null hypothesis:
# 1. The test statistics is greater than 1.96.
# 2. The p-value is less than 0.05.

# In[10]:


get_95_ci(fullbase_yes['price'], fullbase_no['price'])


# With 95% confidence, houses with full basement sells between `$`15,032.29 and `$`5,801.54 more than houses without full basement.

# In[11]:


g = sns.pointplot(data=[fullbase_yes['price'], fullbase_no['price']], join=False)
                        
g.set(xticklabels = ['fullbase_yes', 'fullbase_no'])

