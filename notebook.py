#!/usr/bin/env python
# coding: utf-8

# In[210]:


import pandas
import numpy as np
import matplotlib.pyplot as plt
import csv

#read tweets into python dataframe object

df = pd.read_csv('tweets5.csv')


#Make 3 copies of original CSV -> 1 having all tweets, one only tweets and one only retweets
AllTweets=df
Retweets=df
Tweets=df

#Verify their shape is same

#AllTweets.shape
#Retweets.shape
#OnlyTweet.shape


# In[211]:


Tweets=Tweets[~Tweets.Tweet.str.startswith('RT @')]


# In[212]:


Tweets.shape


# In[213]:


print("Lets see the most frequent tweeter")
Tweets["User_ID"].mode()


# In[214]:


print("How many times did",Tweets["User_ID"].mode(), "tweet to the selected hashtag?")
Tweets["User_ID"].value_counts()[:30]


# In[215]:


Retweets=Retweets[Retweets.Tweet.str.startswith('RT @')]
Retweets.shape


# In[216]:


print("Lets see who is the most frequent retweeter")
Retweets["User_ID"].mode()


# In[217]:


print("How many times did",Retweets["User_ID"].mode(), "tweet to the selected hashtag?")
Retweets["User_ID"].value_counts()[0]


# In[218]:


print("List of top 10 retweeters")
Retweets['User_ID'].value_counts()[0:10]


# In[219]:


#Get number of tweets from Top 10 Retweeters
top10Retweeters={'theAsianBlue','tiengudda','Sully_UTC','LFC_bot_v1','TOWIChelsea','iQFePJb2mVjZP3W','NanaPok21528602','mangkornzzzz_','ChelseaPuzzles','aliabbas1410'}
Tweets_copy = Tweets
Tweets_copy = Tweets_copy[Tweets_copy.User_ID.isin(top10Retweeters)]
Tweets_copy.shape


# In[220]:


Tweets_copy['User_ID'].value_counts()[0:10]


# In[221]:


#Question 1 part 2 : Finding out the top  tweeter
# To do so, we remove the retweets from the original dataframe

tweets_only= df


# In[222]:


print(tweets_only.shape)


# In[223]:


retweet_prefix=['RT @']


# In[224]:


TWEET=tweets_only[~tweets_only.Tweet.str.startswith(tuple(retweet_prefix),na=False)]


# In[225]:


TweetsByTopRetweeters=tweets_only.loc[tweets_only['User_ID'].isin(top10Retweeters)]
TweetsByTopRetweeters['User_ID'].value_counts()


# In[226]:


print("Lets see who is the most frequent tweeter")
TWEET["User_ID"].mode()


# In[326]:


print("List of top 20 tweeters")
#TWEET["User_ID"].value_counts()[0:10]
#tweetsByTop10Retweeters=TWEET[TWEET['User_ID'].isin(top_10_rt_list)]
#tweetsByTop10Retweeters.shape
TWEET["User_ID"].value_counts()[0:20]  


# In[ ]:


#Bots: ChelseaPuzzles, FootyKeyrings, ChelseaRooter, bettngtips, UKBettingoffer, CFCChronicle (has a score of 3.3 and probably has automated text responses), chelsea_poland, 


# In[228]:


print("How many times did 'ChelseaPuzzles' tweet to the selected hashtag?")
TWEET["User_ID"].value_counts()[0]


# In[229]:


print("How many of the tweets in the current dataset were original tweets?")
TWEET.shape[0]


# In[230]:


print("How many of the tweets in the current dataset were retweets?")
rt.shape[0]-TWEET.shape[0]


# In[231]:


print("What was the ratio of tweets to retweets in the data set?")
TWEET.shape[0]/(rt.shape[0]-TWEET.shape[0])


# In[232]:


print("For the pie chart, what was the percentage of original tweets in the dataset?")
(TWEET.shape[0]/rt.shape[0])*100


# In[233]:


print("For the pie chart, what was the percentage of retweets in the dataset?")
((rt.shape[0]-TWEET.shape[0])/rt.shape[0])*100


# In[234]:


print("Let us see the top retweet.")
TOP_RT.Tweet.mode()


# In[235]:


TOP_RT.Tweet.value_counts()[0]


# In[236]:


print ("The percentage of top 10 tweeters tweets in the dataset is approximately 3.39%")
print ("The percentage of top 10 retweeters tweets in the dataset is approximately 11.72%")


# In[ ]:





# In[237]:


geoloc = pd.DataFrame(df,columns=['Twitter_ID','User_ID','Geo_enabled','Location'])


# In[238]:


print("Number of profiles with no geo-location enabled:" ,geoloc.Geo_enabled.isna().sum())


# In[239]:


print("Percentage of profiles with geo-location is ",(3362/6760)*100)


# In[240]:


print("Number of profiles with no location is " ,geoloc.Location.isna().sum())


# In[241]:


print("Percentage of profiles with location is ",(3160/6760)*100)


# In[242]:


print("Top 10 locations from which tweets were sent out")
geoloc.Location.value_counts()[0:11]


# In[243]:


print ("Highest number of followers is =",df.Followers.max())


# In[454]:


#demographic
most_followed_people= df.nlargest(16,columns='Followers')
list_of_most_followed_people= list(most_followed_people['User_ID'])
list_of_most_followed_people


# In[330]:


print("Most followed profiles")
most_followed_people.value_counts()[0:10]


# In[453]:



most_friended_people= df.nlargest(21,columns='Friends')
list_of_most_friended_people= list(most_friended_people['User_ID'])
list_of_most_friended_people


# In[246]:


print ("Highest number of friends is =",df.Friends.max())


# In[247]:


from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
Number=[2248, 4512]
Percentage=[33.25, 66.75]
legend = ['Tweets', 'Retweets']
ax.pie(Percentage, labels = legend,autopct='%1.2f%%')
plt.show()


# In[248]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

Legend = ['Geocode enabled', 'Location']
Percentage = [49.73, 46.75]
ax.set_title('Percentage of geocoded tweets and located profiles')
ax.bar(Legend, Percentage)

plt.show()


# In[ ]:





# In[249]:


list(df)


# In[250]:


original['User_ID'].value_counts()


# In[251]:


def count_elements(seq) -> dict:
    #Tally elements from `seq'.
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
        
    return hist


# In[318]:


tweet_count_frequency= count_elements(original['User_ID'].value_counts())
tweet_count_frequency=dict(tweet_count_frequency)
tweet_count_frequency


# In[334]:


from collections import Counter
from pandas import DataFrame
FrequentWords=dict(Counter(" ".join(df["Tweet"]).split()).most_common(150))


FrequentWords


# In[336]:


print(FrequentWords.keys())


# In[337]:


print(FrequentWords.values())


# In[ ]:


data = []
for row in result_set:
    data.append({'value': row["tag_expression"], 'key': row["tag_name"]})


# In[275]:


from datetime import datetime, timedelta

t = np.arange(datetime(2021,1,15), datetime(2021,1,16), timedelta(minutes=1)).astype(datetime)


# In[276]:


t


# In[277]:


print(t)


# In[279]:


t.shape


# In[281]:


print(df.columns)


# In[282]:


print(df['Date_and_Time'].head())


# In[289]:


dateTimeValues=DataFrame(df['Date_and_Time'])


# In[443]:


dateTimeValues['Frequency']=dateTimeValues['Date_and_Time'].value_counts()


# In[444]:


dateTimeDataFrame=pd.DataFrame(data=dateTimeValues['Date_and_Time'].value_counts(),columns=["Timestamp","Count"])

list(dateTimeDataFrame.columns)


# In[445]:


print(sorted(list(dateTimeDataFrame['Timestamp'])))


# In[446]:


print(dateTimeDataFrame.shape)


# In[447]:


import matplotlib.pyplot as mpl

mpl.plot(dateTimeValues['Date_and_Time'].value_counts().head(1080))


# In[448]:


dateTimeValues.head()


# In[452]:


dateTimeValues.to_csv("dateTime.csv")


# In[ ]:





# In[ ]:




