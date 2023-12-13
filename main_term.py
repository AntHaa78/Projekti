#from sense_hat import SenseHat, ACTION_RELEASED
#import time 
#from gpiozero import MotionSensor
#from datetime import datetime
#from signal import pause
from Modes_term import *

# Main file for working in terminal.
# issues : input staying in terminal, any way to remove directly after entering them? Mostly due to keyboard methods (doesnt press enter). Same issue with sensors?


""" 
global activeMode
activeMode = 1 """



""" sense = SenseHat()
sense.clear()
 """



while True:
	mode_chosen=input("\nPlease choose a mode: (press 'e' at any point to exit the mode)\n1: Room booking\n2: Alert System \n3: Monitoring system \n\n")
	if mode_chosen=="1":
		mode_one()
	if mode_chosen=="2":
		mode_two()
	if mode_chosen=="3":
		mode_three()
	if mode_chosen=="e":
		exit()
	else:
		print("\nCommand not recognised. Please choose 1-3")
