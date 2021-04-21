import tweepy
import json
import psutil
import os


IMG_FILENAME = "/home/pi/image.jpeg"
CONFIG_FILENAME = "/home/pi/solarBot/config.json"

def twitter_api():
    with open(CONFIG_FILENAME) as json_data_file:
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
    snapshot()
    # Write a tweet to push to our Twitter account
    tweet = 'I am alive again!'
    api.update_with_media(IMG_FILENAME, status=tweet)

def uptime():
    return time.time() - psutil.boot_time()

def snapshot():
    cmd = "raspistill -o %s" % IMG_FILENAME
    os.system(cmd)

def main():
    tweet()

if __name__ == "__main__":
    main()

