import tweepy
import datetime
import exampleb as bot

class TwitterAPI:

    def __init__(self):
        '''connect to twitter account'''

        consumer_key = "XXXXXXXXXX"
        consumer_secret = "XXXXXXXXXX"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "XXXXXXXXXX"
        access_token_secret = "XXXXXXXXXX"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        '''post tweet'''

        self.api.update_status(status=message)


def go_tweet():
    '''generate, record, send tweet'''

    twitter = TwitterAPI()
    to_tweet=bot.get_string()
    print(str(datetime.datetime.now()) + " " + to_tweet)
    twitter.tweet(to_tweet)

if __name__ == '__main__':
    
    go_tweet()

