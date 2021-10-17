#!/usr/bin/env python
# coding: utf-8

# # Do pitcher's handedness and batter's handedness matter?
# 
# ## Introduction
# In baseball, "switch hitters" switch their bat stance with the opposite hand from the pitcher. For example, When the Brave's second baseman Ozzie Albies faces a _lefty_ pitcher, he bats _righty_. Switch hitters are deemed valuable for their ability to face any pitcher. Nevertheless, is there a significant advantage for the batters when the pitcher and the batter are opposite-handed? Could it be another "old-school tradition" that baseball players follow? This research will help deep dive into the batters' performance based on the pitcher's handedness. This research will benefit casual baseball fans and sports analysts alike. Because we are using actual data from the 2021 season, and both audiences will find the data relevant and useful.
# 
# ## Research question and hypothesis
# * Research question: Do batters hit better against a pitcher who pitches with the opposite hand?
# * Null hypothesis: There is no significant difference between batters who bat against the pitchers with the same hand versus batters who bat against the pitchers with the opposite hand.
# 
# ## Dataset
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
# ## Method
# First, I will split the dataset into two groups. Then I will check for the normality using histogram, skewness, and kurtosis. Once I analyze the normality of the data, I will use an appropriate statistical test to derive the result. 

# In[ ]:




