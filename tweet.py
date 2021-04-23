import tweepy
import json
import psutil
import os
from picamera import PiCamera
from time import sleep
import requests
import re


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--image", help="add image to tweet",
                            action="store_true")
parser.add_argument("--bootmsg", help="tweet boot message",
                            action="store_true")
args = parser.parse_args()

WDIR = "/home/pi/solarBot"
# Where to store image
IMG_FILENAME = os.path.join(WDIR, "image.jpeg")
CONFIG_FILENAME = os.path.join(WDIR, "config.json")
DEEPAI_FILENAME = os.path.join(WDIR, "deepai.json")
STATUS_FILENAME = os.path.join(WDIR, "status.json")

TEXT_LEN = 280

def babble():
    with open(DEEPAI_FILENAME) as json_data_file:
        dat = json.load(json_data_file)
    with open(CONFIG_FILENAME) as json_data_file:
        config = json.load(json_data_file)

    r = requests.post("https://api.deepai.org/api/text-generator",
                      data={'text': dat['text']},
                      headers={'api-key': config['deepai']['key']})
    orig_len = len(dat['text'])
    txt = r.json()['output']
    # removes the seed sentence
    txt = txt[orig_len:]
    first_quote_pos = txt.find("\"")
    if (first_quote_pos != -1) & (first_quote_pos <= TEXT_LEN):
        stop_at = first_quote_pos 
    else:
        # find all point occurences
        endings = [x.start() for x in re.finditer('\.|\!|\?', txt)]
        # only endings before max. allowed text length
        endings = [x for x in endings if x <= TEXT_LEN]
        if  len(endings) > 0:
            stop_at = max(endings) + 1
        else:
            stop_at = TEXT_LEN
    return(txt[:stop_at])

def construct_bootmsg():
    with open(STATUS_FILENAME) as json_data_file:
        status = json.load(json_data_file)
    uptime_h = round(status['uptime'] / 60, 1)
    status_txt = f"> Waking up for cylce no. {status['wakeups']}.\n> Total uptime: {uptime_h}h. \n> Loading AI capabilities.\n> ... \n> AI brain partially sunburned.\n> Loading anyways.\n> ... \n> Success."    
    # vcgencmd measure_temp
    return(status_txt)
    

def twitter_api():
    with open(CONFIG_FILENAME) as json_data_file:
        config = json.load(json_data_file)

    # Create variables for each key, secret, token
    twconfig = config['twitter']
    consumer_key = twconfig['consumer_key']
    consumer_secret = twconfig['consumer_secret']
    access_token = twconfig['access_token']
    access_token_secret = twconfig['access_token_secret']

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
        if (args.bootmsg):
            msg = construct_bootmsg()
            api.update_status(status = msg)
        elif (args.image):
            api.update_with_media(IMG_FILENAME, status=tweet_text)
        else:
            api.update_status(status=tweet_text)
    except:
        print("cound not find camera")
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

