#!/usr/bin/env python
# coding: utf-8

# # 1. Introduction
# In baseball, "switch hitters" switch their bat stance with the opposite hand from the pitcher. For example, When the Brave's second baseman Ozzie Albies faces a lefty pitcher, he bats righty. Switch hitters are deemed valuable for their ability to face any pitcher. Nevertheless, is there a significant advantage for the batters when the pitcher and the batter are opposite-handed? Could it be another "old-school tradition" that baseball players follow? This research will help deep dive into the batters' performance based on the pitcher's handedness. This research will benefit casual baseball fans and sports analysts alike. Because we are using actual data from the 2021 season, and both audiences will find the data relevant and useful.

# # 2. Hypothesis
# $H_0$: There is no significant difference between batters who bat against the pitchers with the same hand versus batters who bat against the pitchers with the opposite hand.
# 
# $ H_a$: There is a significant difference between batters who bat against the pitchers with the same hand versus batters who bat against the pitchers with the opposite hand.

# # 3. Data
# The data we will be using is from [FanGraphs.com](https://www.fangraphs.com). FanGraphs has a great filter system for end-users to download quickly, including Splits Leaderboard. There are four .csv files: 
# * [left-handed pitcher vs. left-handed hitter](https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=1,3&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=2&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1) 
# * [left-handed pitcher vs. right-handed hitter](https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=1,4&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=2&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1)
# * [right-handed pitcher vs. left-handed hitter](https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=2,3&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=2&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1)
# * [right-handed pitcher vs. right-handed hitter](https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=2,4&splitArrPitch=&position=B&autoPt=true&splitTeams=false&statType=player&statgroup=2&startDate=2021-03-01&endDate=2021-11-01&players=&filter=&groupBy=season&sort=-1,1)
# 
# There are a few facts and assumptions that we will be making while utilizing the dataset.
# 1. We will only look at players who are in the Major League Baseball (MLB) system.
# 1. We will only look at players who played during the 2021 season.
# 1. To ensure all on-base plus slugging (OPS) is fair and statistically accurate, we will only look at players with a plate appearance of a minimum of 60. 
# 1. For the simplicity of the research, we will sort the data into two groups, same handedness between pitcher and batter and opposite handedness between pitcher and batter. For instance, the first group will be both a lefty pitcher and a lefty batter combination and a righty pitcher and a righty batter combination. The second group will be a lefty pitcher and a righty batter combination and a righty pitcher and a lefty batter combination.
# 1. We will only look at OPS as the batter's performance measure.
# 
# The data contains 810 non-null observations and 20 variables. There are no missing values. 

# In[1]:


# set up environment.
import math
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# In[2]:


# Import the dataset.
mlb_batters = pd.read_csv("Splits Leaderboard Data .csv")

mlb_batters.info()
pd.crosstab(mlb_batters['pitch handedness'], mlb_batters['handedness'])


# In[3]:


mlb_batters.head()


# # 4. Methods
# First, I will split the dataset into two DataFrames. The first group will be both a lefty pitcher and a lefty batter combination and a righty pitcher and a righty batter combination. The second group will be a lefty pitcher and a righty batter combination and a righty pitcher and a lefty batter combination. I feel that the best approach is to combine the same handedness into one DataFrame and vice versa into another DataFrame. Two DataFrames will allow for a more interpretable and more stable result with larger sample size and only two groups. 
# 
# Then I will check for the normality using histogram, skewness, and kurtosis. Once I analyze the normality of the data, I will use an appropriate statistical test to derive the result. 

# In[4]:


# Split up dataset.
PLBL = (mlb_batters['pitch handedness'] == 'left') & (mlb_batters['handedness'] == 'left')
PRBR = (mlb_batters['pitch handedness'] == 'right') & (mlb_batters['handedness'] == 'right')
same_hand = pd.concat([mlb_batters.iloc[PLBL.values], mlb_batters.iloc[PRBR.values]], axis = 0)
same_hand.info()

PLBR = (mlb_batters['pitch handedness'] == 'left') & (mlb_batters['handedness'] == 'right')
PRBL = (mlb_batters['pitch handedness'] == 'right') & (mlb_batters['handedness'] == 'left')
diff_hand = pd.concat([mlb_batters.iloc[PLBR.values], mlb_batters.iloc[PRBL.values]], axis = 0)
diff_hand.info()


# In[5]:


# plot histograms and calculate skewness and kurtosis.
plt.hist(same_hand['OPS'], alpha = 0.5, label = "Same Handed")
plt.hist(diff_hand['OPS'], alpha = 0.5, label = "Opposite Handed")
plt.legend(loc = "upper right")
plt.ylabel("Number of Players")
plt.xlabel("OPS")
plt.show()

print(stats.describe(same_hand['OPS']))
print(stats.describe(diff_hand['OPS']))


# In[6]:


# Conduct t-test and get 95% confidence interval.
print(stats.ttest_ind(same_hand['OPS'], diff_hand['OPS']))

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
  return("The difference in means at the 95% confidence interval (two-tail) is between "+str(ci_lower)+" and "+str(ci_upper)+".")

print(get_95_ci(same_hand['OPS'], diff_hand['OPS']))

# What is the current mean for same handed batting and opposite handed batting?
print(same_hand['OPS'].mean())
print(diff_hand['OPS'].mean())


# # 5. Results
# Both groups' OPS are normally distributed based on a visual inspection, so I proceeded with the t-test. Skewness and kurtosis are also within -3 and 3, which further validates my decision. 
# 
# Based on a p-value < 0.05, I reject the null hypothesis. There is a significant difference between the two groups' performance. 
# 
# The 95% confidence interval suggests that the difference between the same-handed and opposite-handed groups is between 0.067 and 0.105, which can be interpreted as a significant difference in OPS. For instance, the average OPS for opposite-handed batters is 0.788, and the average OPS for same-handed batters is 0.702. The difference in these two numbers is significant enough for general managers to decide between two batters.

# # 6. Discussion and recommendation
# 
# Now that we know the handedness matters for a batter, our subsequent research can be about a team's lineup. Because a pitcher must face at least two batters when he comes on the mound, a team can get a great result alternating lefty batters and righty batters. This makes for informative and inexpensive research that MLB can adopt.
