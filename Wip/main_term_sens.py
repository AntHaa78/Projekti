#from sense_hat import SenseHat, ACTION_RELEASED
#import time 
#from gpiozero import MotionSensor
#from datetime import datetime
#from signal import pause
from modes_term_sens2 import *

#sense = SenseHat()
#sense.clear()

# Main file for working in terminal.
# issues : input staying in terminal, any way to remove directly after entering them? Mostly due to keyboard methods (doesnt press enter). Same issue with sensors?

blue = (0,0,255)
green = (0, 255, 0)
red = (255, 0, 0)


#initAnimation() change
while True:
	#mode_chosen=input("\nPlease choose a mode: (press 'e' at any point to exit the mode)\n1: Room booking\n2: Alert System \n3: Monitoring system \n\n")
	mode_chosen=input("\nPlease choose a mode: \n1: Room booking\n2: Alert System \n3: Monitoring system \n4: Traffic Counter \n\n'e' to exit.")
	if mode_chosen=="1":
		sense.show_letter(mode_chosen,blue)
		mode_one()
		#sense.clear()
	if mode_chosen=="2":
		sense.show_letter(mode_chosen,blue)
		mode_two()		
	if mode_chosen=="3":
		sense.show_letter(mode_chosen,blue)
		mode_three()
	if mode_chosen=="4":
		sense.show_letter(mode_chosen,blue)
		mode_four()
	if mode_chosen=="e":
		sense.clear()
		exit()
	else:
		print("\nCommand not recognised. Please choose 1-4")
