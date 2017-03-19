#!/bin/bash

printMsg(){
echo "===================================================="
echo "= " $1
echo "===================================================="
}

printMsg "Updating apt-get."
apt-get update

# Install Pigpio
printMsg "Installing Pigpiod"
apt-get install pigpio -y

# Install apache and php
printMsg "Install web server"
apt-get install apache2 -y
apt-get install php5 libapache2-mod-php5 -y

# Copy the web folder content to the new web root
printMsg "Copying web files to web root."
rm /var/www/html/index.html
cp -R web/* /var/www/html
chown -R www-data:www-data /var/www/html

# Grant sudo access to www-data
printMsg "Enabling sudo access for web server user."
cat  > /etc/sudoers.d/020_www-data-nopasswd << EOF
www-data ALL=(ALL) NOPASSWD: /sbin/iwconfig, /sbin/iwlist, /bin/grep
EOF

# Set up a ramdrive for temp files/inter process comms
printMsg "Enabling ram disk in fstab."
if [ ! -d "/mnt/ramdisk" ]; then
	mkdir /mnt/ramdisk
fi

if grep -q "/mnt/ramdisk" /etc/fstab; then
echo "/mnt/ramdisk already in fstab"
else
cat >> /etc/fstab << EOF
tmpfs       /mnt/ramdisk tmpfs   nodev,nosuid,noexec,nodiratime,size=1M   0 0
EOF
fi

# Start github library clones tasks.
printMsg "Cloning required libraries for python scripts."
mkdir /home/pi/GitHub
cd /home/pi/GitHub

# OLED library
printMsg "Getting OLED library."
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
python Adafruit_Python_SSD1306/setup.py

# Ensure pigpiod is started at boot.


# REMOVED
## Set up an access point for initial configuration
#apt-get install hostapd -y
#apt-get install dnsmasq -y
#service hostapd stop
#service dnsmasq stop
#cp includedFiles/hostapd.conf /etc/hostapd/hostapd.conf
#cp includedFiles/interfaces /etc/network/interfaces
#cp includedFiles/autohotspot /usr/bin/autohotspot
#chmod +x /usr/bin/autohotspot
#cp includedFiles/autohotspot.service /etc/systemd/system/autohotspot.service
#service autohotspot start
