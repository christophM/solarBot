import tweepy
import json
import psutil
import sys

def twitter_api():
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
 
    # Create variables for each key, secret, token
    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']
    access_token = config['access_token']
    access_token_secret = config['access_token_secret']

    # Set up OAuth and integrate with API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)



def tweet():
    api = twitter_api()
    filename = sys.argv[1]
    # Write a tweet to push to our Twitter account
    tweet = 'I am alive again!'
    api.update_with_media(filename, status=tweet)

def uptime():
    return time.time() - psutil.boot_time()



def main():
    tweet()

if __name__ == "__main__":
    main()

