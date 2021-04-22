# Solar-powered Raspberry Pi Twitter Bot



## Software Requirements
SimpleCV for images
Python3

## pip modules
psutil
tweepy
certifi

Add to crontab:





# Hardware to Buy

- A pi zero WH
- Micro USB cable, which you might already have
- Case for the pi zero WH to protect from weather
- Solar panel with USB output
- Camera module (TODO: link)
- if pi will be deployed without WiFi access
	- dongle for SIM card
        - Sim card and data plan

# Setup

## Install Raspbian and setup Pi

## Add Camera

- Connect camera to pi
- `sudo raspi-config` and enable camera in 'Interfacing Options' 

## Connect with Github

- create Github account (ideally new one just for the bot)
- setup ssh
- Clone repo
- 

## Setup Twitter

- Add config.json with list {"consumer_key", "consumer_secret", "access_token", "access_token_secret"}
- 

## Setup Language Model

- Get DeepAI account and API-key

## Give IP address

- Install noip2 (TODO: how?)

## Deploy 

- type `crontab -e` and add:  
`@reboot sudo /usr/local/bin/noip2
 @reboot /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/tweet.py
`
- the first line sets ip address
- the second line tweets after reboot
 
