import twitter,json, sys, csv
# got my keys!
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth, retry=True)

# writing to a newly created file within the destination folder
csvfile = open('tweets5.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

#  heres a function that takes out characters that can break
#  our import into Excel and replaces them with spaces
#  it also does the unicode bit
def clean(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val
    return clean


q = "#CFC" # refer to reflective essay
print ('Filtering the public timeline for keyword="%s"' % (q,))

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:
    # print json.dumps(tweet)
    try:
        if tweet['truncated']:
            tweet_text = tweet['extended_tweet']['full_text']
        else:
            tweet_text = tweet['text']
    # values for required questions posed in the assessment
    # refer to week7 exercises to segregate data accordingly
        csvwriter.writerow([tweet['id_str'],
                            tweet['created_at'],
                            clean(tweet['user']['screen_name']),
                            clean(tweet_text),
                            tweet['user']['created_at'],
                            tweet['user']['followers_count'],
                            tweet['user']['friends_count'],
                            tweet['user']['statuses_count'],
                            clean(tweet['source']),
                            clean(tweet['user']['location']),
                            tweet['user']['geo_enabled'],
                            tweet['user']['lang'],
                            clean(tweet['user']['time_zone'])
                            ])
        print (tweet_text).encode("utf-8")
    except Exception as err:
        print (err)
        pass
