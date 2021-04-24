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

## Setup GSM stick

- Connect stick
- check with `lsusb` that Huawei Stick is detected
- `sudo apt install usb-modeswitch usb-modeswitch-data`
- https://tutorials-raspberrypi.com/raspberry-pi-gsm-module-mobile-internet-lte-3g-umts/


## Setup Reverse SSH

This is only necessary when 3G is used.

- https://zieren.de/raspberry-pi/reverse-ssh-through-3gnat/

## Give IP address

- Install noip2 (TODO: how?)
- https://www.blackmoreops.com/2020/11/18/how-to-install-the-noip2-on-ubuntu-and-run-via-systemd-systemctl-noip-dynamic-update-client/

## Deploy 

- type `crontab -e` and add:  
```
@reboot sleep 300 && cd /home/pi/solarBot/; git pull
@reboot /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/tweet.py --boot
@reboot /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/tweet.py --image
@reboot /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/increase-wakeup.py 
*/10 * * * * /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/tweet.py &
*/5  * * * * /home/pi/solarBot/venv/bin/python3 /home/pi/solarBot/increase-uptime.py 
```
- the first line sets ip address
- the second line tweets after reboot
 
