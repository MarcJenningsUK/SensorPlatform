#!/bin/bash
#apt-get update

## Install apache and php
#apt-get install apache2 -y
#apt-get install php5 libapache2-mod-php5 -y

## Copy the web folder content to the new web root
#rm /var/www/html/index.html
#cp -R web/* /var/www/html

## Grant sudo access to www-data
#cat  > /etc/sudoers.d/020_www-data-nopasswd << EOF
#www-data ALL=(ALL) NOPASSWD: /sbin/iwconfig, /sbin/iwlist, /bin/grep
#EOF

## Set up an access point for initial configuration
#apt-get install hostapd -y
#apt-get install dnsmasq -y

service hostapd stop
service dnsmasq stop

cp includedFiles/hostapd.conf /etc/hostapd/hostapd.conf
cp includedFiles/interfaces /etc/network/interfaces
cp includedFiles/autohotspot /usr/bin/autohotspot
chmod +x /usr/bin/autohotspot

cp includedFiles/autohotspot.service /etc/systemd/system/autohotspot.service
service autohotspot start
