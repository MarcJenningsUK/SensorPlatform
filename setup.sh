#!/bin/bash

printMsg(){
echo "===================================================="
echo "= " $1
echo "===================================================="
}

printMsg "Updating apt-get."
apt-get update > /tmp/tmp.txt 2>&1

# Install Pigpio
printMsg "Installing Pigpiod"
apt-get install pigpio -y >> /tmp/tmp.txt 2>&1

# Install apache and php
printMsg "Install web server"
apt-get install apache2 -y >> /tmp/tmp.txt 2>&1
apt-get install php5 libapache2-mod-php5 -y >> /tmp/tmp.txt 2>&1

# Copy the web folder content to the new web root
printMsg "Copying web files to web root."
rm /var/www/html/index.html
cp -R /home/pi/SensorPlatform/web/* /var/www/html
chown -R www-data:www-data /var/www/html
touch /home/pi/SensorPlatform/configuration.conf
chown pi:pi /home/pi/SensorPlatform/configuration.conf
chmod 666 /home/pi/SensorPlatform/configuration.conf

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
git clone https://github.com/adafruit/Adafruit_Python_SSD1306 >> /tmp/tmp.txt 2>&1
python Adafruit_Python_SSD1306/setup.py install >> /tmp/tmp.txt 2>&1

# OLED pre-requisites.
printMsg "Getting OLED pre-requisites."
sudo apt-get update >> /tmp/tmp.txt 2>&1
sudo apt-get install build-essential python-dev python-pip python-imaging python-smbus -y >> /tmp/tmp.txt 2>&1
sudo pip install RPi.GPIO -y >> /tmp/tmp.txt 2>&1
