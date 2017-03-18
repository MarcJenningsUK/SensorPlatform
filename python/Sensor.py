import time
import decimal
import RPi.GPIO as GPIO
import Adafruit_SSD1306
import urllib2
import HTU21DF

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

RST = 4
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
width = disp.width
height = disp.height
buttonpin = 21
displaymode = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonpin, GPIO.IN, GPIO.PUD_DOWN)

brandimage = Image.open('branding.png').convert('1')
disp.image(brandimage)
disp.display()
time.sleep(3)

disp.clear()
disp.display()
image = Image.new('1', (width, height))
font = ImageFont.truetype('segoe-wp.ttf', 24)
draw = ImageDraw.Draw(image)

measuredTemp = 0
measuredHumidity = 0

readEvery = 10 # Seconds between readings
reportEvery = 30 # log data every Nth reading
reportCount = reportEvery

def buttonHandler(channel):
    global displaymode
    if displaymode == 0:
        displaymode = 1

def ReadSensors():
    global measuredTemp 
    global measuredHumidity
    global reportCount
    global reportEvery

    measuredTemp = HTU21DF.read_temperature()
    measuredHumidity = HTU21DF.read_humidity()
    displayValues(str(round(measuredTemp, 1)) + " deg C", str(round(measuredHumidity, 1)) + " %")

    if(reportCount == reportEvery):
        # Send data to the web service
        reqString = 'http://api.marc-jennings.co.uk/InsecureUploadOfData.php?temperature=' + str(measuredTemp) + '&humidity=' + str(measuredHumidity)
        req = urllib2.Request(reqString)
        resp = urllib2.urlopen(req)

    reportCount = reportCount + 1	
    if(reportCount > reportEvery):
        reportCount = 1

def displayValues(line1, line2):
    global displaymode
    if displaymode == 1:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        disp.image(brandimage)
    else:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((0, 0), line1, font=font, fill=255)
        draw.text((0, 32), line2, font=font, fill=255)
        # Draw the image buffer.
        disp.image(image)
 
    disp.display()
    displaymode = 0

GPIO.add_event_detect(buttonpin, GPIO.RISING, callback=buttonHandler, bouncetime=100)

while True:
    ReadSensors()
    time.sleep(readEvery)
