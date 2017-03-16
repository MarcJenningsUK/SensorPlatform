#!/bin/bash

if [ -f /etc/wpa_supplicant/wpa_supplicant.conf ]
then
	cat /etc/wpa_supplicant/wpa_supplicant.conf | grep ssid | sed -e 's/^[ \t]*//' | sed -e 's/ssid="//' | sed 's/"//'
fi
