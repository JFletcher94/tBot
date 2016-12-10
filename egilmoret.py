import tweepy
import datetime
import egilmoreb as bot

class TwitterAPI:

    def __init__(self):
        '''connect to twitter account'''

        consumer_key = "fabgY4JS6iOJnWhH3zupf8iM6"
        consumer_secret = "euKy2acLsNz4NnANQu8F4pNaGqsTMBjyIKTv2g7UA9WECZRjGD"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3438838661-HcsCTdPcCl0nNyruUtQELxTEl3c8Q88R1qZRbwX"
        access_token_secret = "dePf2ZG8qC79gR9QTQiTAuSJ60hVO30KGv2FTAnVN0I7y"
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

