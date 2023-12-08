#from sense_hat import SenseHat, ACTION_RELEASED
#import time 
#from gpiozero import MotionSensor
#from datetime import datetime
#from signal import pause
from Modes import *


global activeMode
activeMode = 1



sense = SenseHat()
sense.clear()


print("Please choose a mode \n1: Room booking\n2: Alert System \n3: Monitoring system \n")
while True:
	for event in sense.stick.get_events():
			#print(event.direction, event.action)
		if event.action == "pressed":
			if event.direction == "up":
				print("\n")
				#print(activeMode)
				print("\n")
					#print("Are you sure?")
					#mode1() testausta varten
				if activeMode == 1:
					print("\nRoom booking mode chosen")
						#run mode 1
					mode1()
				elif activeMode == 2:
					print("\nAlert mode chosen")
					modeTwo()
				elif activeMode == 3:
					print("Monitoring system chosen")
					modeThree()
				else:
					print("This shouldn't be happening!")
			if event.direction == "down":
				print("down")
			if event.direction == "left":
				if activeMode > 1:
					activeMode = activeMode - 1
				sense.show_letter(str(activeMode),[200,0,0],[75,(375-activeMode*125),((activeMode*125)-125)])
			if event.direction == "right":
				if activeMode < 3:
					activeMode = activeMode + 1
				sense.show_letter(str(activeMode),[200,0,0],[75,(375-activeMode*125),((activeMode*125)-125)])

sense.clear()
