# Mode alarm when motion detected

# When person leaves, can activate alarm mode
# If motion detected -> alarm
# Enter password to desactivate alarm

from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
#from sense_hat import Sensehat

sense = SenseHat()
pir1= MotionSensor(18)
pir2 = MotionSensor(17) 


#alarm_mode = 0

#def alarm_message():
#    sense.show_message("INTRUDER!!!")


password = "abc123"

if mode_chosen==2:
    while True:
        sense.show_message("ALARM ON!")
        if pir1.motion_detected == True or pir2.motion_detected == True:
            sense.show_message("INTRUDER!!!")
            while True:
                answer = input("Please enter password to desactivate alarm: ")
                if answer == password:
                    print("Alarm desactivated, back to alarm mode")
                    break
                else:
                    print("Wrong password, alarm still beeping")
            sense.show_message("ALARM ON!")
