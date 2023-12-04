from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
from sense_hat import Sensehat

sense = SenseHat()
sense.set_rotation(180)

pir1= MotionSensor(18)
pir2 = MotionSensor(17)

lastmotion = 0       
motion5s = 0

def going_in():
    while True:
        if pir1.motion_detected == True:
            lastmotion = time.time()
        motionseconds = time.time() - lastmotion      # Get the amount of time since last motion
        if motionseconds < 5:
        motion5s = 1                   #set the motion in last 5 seconds variable to true
        elif motionseconds >= 5:
        motion5s = 0                   #set the motion in last 5 seconds variable to false
        if motion5s == True:
        print ("Motion was detected in last 5 seconds, was detected %0.10f " %(motionseconds) + " ago.")
        elif motion5s == False:
        print ("No motion detected within last 5 seconds, was detected %0.10f " %(motionseconds) + " ago.")
        time.sleep(0.25)           #quaarter second delay    


mode_chosen=int(input("Please choose a mode (1-3): "))

if mode_chosen==1:
    going_in()

def print_going_in():
    print("GOING IN")

def going_in():
    lastmotion = time.time()
    motionseconds = time.time() - lastmotion 
    pir1.close()
    while motionseconds<5:
        motion5s = 1
        pir2.when_motion = print_going_in
    
