import time

line1 = "defl1"
line2 = "defl2"
image = "defimg"
singleLine = "defSL5"
displayMode = 0

def Display():
	global line1
	global line2
	global image
	global singleLine
	print("=====================")
	if(displayMode == 0):
		print(line1)
		print(line2)
	elif(displayMode == 1):
		print(image)
	elif(displayMode == 2):
		print(singleLine)
	else:
		print("unknown")

def set2Lines(l1, l2):
	global line1
	global line2
	line1 = l1
	line2 = l2
	Display()

def setSingleLine(l1):
	global singleLine
	singleLine = l1
	Display()

def setImage(im):
	global image
	image=im
	Display()

def setDisplayMode(newMode):
        global displayMode
        displayMode = newMode
        Display()

set2Lines("hello","world")
time.sleep(2)
set2Lines("and", "again")
time.sleep(2)
setSingleLine("not yet")
time.sleep(2)
setDisplayMode(2)
time.sleep(2)
setImage("filename.bmp")
setDisplayMode(1)
time.sleep(2)
setDisplayMode(0)
time.sleep(2)
setDisplayMode(2)
time.sleep(2)

print("done")
