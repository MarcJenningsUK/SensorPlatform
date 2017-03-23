import time

temp = "1"
humid = "2"
image = "defimg"
ipAddress = "3"
copyrightText = "©2017 Marc Jennings"

tempSuffix = "°C"
humidSuffix = "%"

displayMode = 0

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
	print("====================")
	# display 2 lines
	if(displayMode == 0):
		print(temp + tempSuffix)
		print(humid + humidSuffix)
	# display just temperature
	elif(displayMode == 1):
		print(temp + tempSuffix)
	# display just humidity
	elif(displayMode == 2):
		print(humid + humidSuffix)
	# display ip address
	elif(displayMode == 3):
		print(ipAddress)
	# display branding image
	elif(displayMode == 4):
		print(image)
	# display copyright notice
	elif(displayMode == 5):
		print(copyrightText)
	else:
		print("unknown")
		
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
setImage("filename.bmp")
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


print("done")
