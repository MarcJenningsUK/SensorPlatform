import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

temp = "1"
humid = "2"
image = "branding.png"
ipAddress = "3"
copyrightText = "©2017 Marc Jennings"

tempSuffix = "°C"
humidSuffix = "%"

displayMode = 0

# set up the oled.
RST = 4
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
width = disp.width
height = disp.height
disp.clear()
disp.display()
image = Image.new('1', (width, height))
font = ImageFont.truetype('segoe-wp.ttf', 24)
bigfont = ImageFont.truetype('segoe-wp.ttf', 48)
draw = ImageDraw.Draw(image)


# MODES
# 0 - temp and humidity
# 1 - just temp
# 2 - just humidity
# 3 - IP Address
# 4 - branding
# 5 - copyright

validNodeCount = 6

def Display():
	global temp
	global humid
	global image
	global ipAddress
	global image
	
	# display 2 lines
	if(displayMode == 0):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				draw.text((0, 0), temp + tempSuffix, font=font, fill=255)
				draw.text((0, 32), humid + humidSuffix, font=font, fill=255)
				disp.image(image)
	
	# display just temperature
	elif(displayMode == 1):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				draw.text((0, 0), temp + tempSuffix, font=bigfont, fill=255)
				disp.image(image)
	
	# display just humidity
	elif(displayMode == 2):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				draw.text((0, 0), humid + humidSuffix, font=bigfont, fill=255)
				disp.image(image)
	
	# display ip address
	elif(displayMode == 3):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				draw.text((0, 0), ipAddress, font=bigfont, fill=255)
				disp.image(image)
	
	# display branding image
	elif(displayMode == 4):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				disp.image(brandimage)
	
	# display copyright notice
	elif(displayMode == 5):
				draw.rectangle((0,0,width,height), outline=0, fill=0)
				draw.text((0, 0), copyrightTest, font=font, fill=255)
				draw.text((0, 32), "All Rights Reserved", font=font, fill=255)
				disp.image(image)
	
	else:
				disp.clear()
				disp.display()
				
def set2Lines(l1, l2):
	global temp
	global humid
	temp = l1
	humid = l2
	Display()
	
def setIpAddress(l1):
	global ipAddress
	ipAddress = l1
	Display()
	
def setImage(im):
	global image
	image=im
	Display()
	
def setDisplayMode(newMode):
		global displayMode
		displayMode = newMode
		Display()

def incrementDisplayMode():
		global displayMode
		global validNodeCount
		displayMode = (displayMode + 1) % validNodeCount
		Display()
		
# MODES
# 0 - temp and humidity
# 1 - just temp
# 2 - just humidity
# 3 - IP Address
# 4 - branding
# 5 - copyright

setDisplayMode(0)
set2Lines("21.1","47")
time.sleep(2)
set2Lines("and", "again")
time.sleep(2)
setIpAddress("192.168.1.3")
time.sleep(2)
setDisplayMode(3)
time.sleep(2)
setImage("branding.png")
setDisplayMode(4)
time.sleep(2)
setDisplayMode(0)
time.sleep(2)
setDisplayMode(2)
time.sleep(2)
setDisplayMode(3)
time.sleep(2)

incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)
incrementDisplayMode()
time.sleep(0.5)

disp.clear()
disp.display()

