""" AIM: After choosing mode1, select booking room mode
- Implement boooking system. Ask user name and time, gives random password.


- Activate sensor 1 around time given. When sensor 1 detects motion, ask user for code.
- turn off sensor 1, activate sensor 2. Whenever detects motion, "reclose" door and will ask for pw again. pw only working for time given.
- turn off sensor 2 at end time, reactivate sensor 1 for  next user. make sure room is empty


 """

""" lastmotion = 0       
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
        pir2.when_motion = print_going_in """

""" from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
from sense_hat import Sensehat
"""
import random
import string

"""
sense = SenseHat()
sense.set_rotation(180)

pir1= MotionSensor(18)
pir2 = MotionSensor(17) """

def reservation():
    pass

def password_generator():
    letters = string.ascii_lowercase
    result_pw = ''.join(random.choice(letters) for i in range(5))
    return result_pw
    #print(f"Your username is {nameassociated} and your password is {result_pw}")

mode_chosen=int(input("Please choose a mode \n1: Room booking\n2: Alert System \n3: Monitoring system \n"))

if mode_chosen==1:

    print("Welcome to the room reservation system")
    name=input("\nEnter your name: ")
    start_time = int(input("\nEnter the start time of the reservation (8-19): "))
    end_time = int(input(f"\nEnter the end time of the reservation ({start_time+1}-20): "))
    password = password_generator()
    print(f"Your name is {name}, your password will be '{password}', your reservation starts at {start_time} and ends at {end_time}")


    
