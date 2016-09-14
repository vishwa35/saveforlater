from keys import keys
import tweepy, sys, datetime, time, math

class saveforlaterbot:
    def __init__(self):
        CONSUMER_KEY = keys['consumerKey']
        CONSUMER_SECRET = keys['consumerSecret']
        ACCESS_KEY = keys['accessKey']
        ACCESS_SECRET = keys['accessSecret']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api= tweepy.API(auth)

    def tweet(self, id, tweetText):
        self.api.update_status(tweetText,in_reply_to_status_id=id)

    def search(self, searchText):
        self.api.search(text=searchText)

bot = saveforlaterbot()
tweets = bot.api.search(q='@saveforlaterbot')
readyTweets = []
for tweet in tweets:
    created_at = tweet.created_at
    #print ("found tweet")
    if(time.time() - (tweet.created_at - (datetime.datetime(1970,1,1))).total_seconds() > 2.16*math.pow(10,7)):
        readyTweets.append(tweet)

for tweet in readyTweets:
    id = tweet.id_str
    username = tweet.user.screen_name
    bot.tweet(id,tweetText='@'+username+' Reminder! Read this tweet again.')
    #time.sleep(10)
