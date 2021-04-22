import tweepy
import json
import psutil
import os
from picamera import PiCamera
from time import sleep
import requests

# Where to store image
IMG_FILENAME = "/home/pi/image.jpeg"
CONFIG_FILENAME = "/home/pi/solarBot/config.json"
DEEPAI_FILENAME = "/home/chris/repos/solarBot/deepai.json"

TEXT_LEN = 280
def babble():
    with open(DEEPAI_FILENAME) as json_data_file:
        dat = json.load(json_data_file)
    r = requests.post("https://api.deepai.org/api/text-generator",
                      data={'text': dat['text']},
                      headers={'api-key': dat['api-key']})
    orig_len = len(dat['text'])
    txt = r.json()['output']
    # removes the seed sentence
    txt = txt[orig_len:]
    first_quote_pos = txt.find("\"")
    if first_quote_pos <= TEXT_LEN:
        stop_at = first_quote_pos
    else:
        stop_at = TEXT_LEN
    return(txt[:stop_at])


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
    try:
        snapshot()
        # Write a tweet to push to our Twitter account
        tweet_text = babble()
        api.update_with_media(IMG_FILENAME, status=tweet_text)
    except:
        tweet = 'Ah darn, waking up and my cam is broken =['
        api.update_status(status=tweet)

def uptime():
    return time.time() - psutil.boot_time()

def snapshot():
    camera = PiCamera()
    # Sleep necessary to adjust lense for brightness
    camera.start_preview()
    sleep(2)
    camera.capture(IMG_FILENAME)
    camera.stop_preview()

def main():
    tweet()

if __name__ == "__main__":
    main()

