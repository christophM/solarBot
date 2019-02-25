import tweepy
import json
import psutil
from cv2 import *

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
    filename = "image.jpeg"
    # Write a tweet to push to our Twitter account
    tweet = 'I am alive again!'
    api.update_with_media(filename, status=tweet)

def uptime():
    return time.time() - psutil.boot_time()


def snapshot():
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("image.jpeg",img) #save image


def main():
    snapshot()
    tweet()

if __name__ == "__main__":
    main()

