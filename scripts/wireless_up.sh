#! /bin/bash

sudo ifconfig wlan0 up
sudo wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant2.conf
sudo dhclient wlan0
