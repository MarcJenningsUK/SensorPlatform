<?php
        system("whoami");
        system("sudo iwlist wlan0 scan | grep ESSID | sed 's/ESSID://' | sed -e 's/^[ \t]*//'");
?>
