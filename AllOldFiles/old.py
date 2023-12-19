# Contain all old functions variables etc
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

from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

lastmotion = 0
motion5s = 0

pir1= MotionSensor(18)
pir2 = MotionSensor(17)

password = "abc123"

def print_going_in():
    print("Motion detected from other sensor, GOING IN")

def going_direction(num):
    lastmotion = time.time()        
    while True:
        motionseconds = time.time() - lastmotion 
        print("Motion detected at",lastmotion)
        #pir1.close()
        if motionseconds<3:
            motion5s = 1
        #motionseconds = time.time() - lastmotion 
            print(motionseconds)
            #pir2.when_motion = print_going_in
            if num == 1 and pir2.motion_detected == True:
                    print("GOING IN")
                    return 1
            if num == 2 and pir1.motion_detected == True:
                    print("GOING OUT")
                    return -1             
        else:
            print("No motion detected from other sensor, exiting")
            return 0
        time.sleep(0.25)
    #
    exit()


# ~ def going_in():
    # ~ pir1= MotionSensor(18)
    # ~ pir2 = MotionSensor(17)
    # ~ lastmotion = 0       
    # ~ #motion5s = 0
    # ~ while True:
        # ~ if pir1.motion_detected == True:
            # ~ lastmotion = time.time()
            # ~ motionseconds = time.time() - lastmotion      # Get the amount of time since last motion
            # ~ #pir1.close()
            # ~ if motionseconds < 5 and pir2.motion_detected== True:
            # ~ #motion5s = 1   
                # ~ print("Motion at sensor 2 was detected, MOVING IN!!!")                #set the motion in last 5 seconds variable to true
            # ~ elif motionseconds < 5 and pir2.motion_detected== False:
            # ~ #motion5s = 0                   #set the motion in last 5 seconds variable to false
                # ~ print("Awaiting motion from sensor 2")
            # ~ elif motionseconds>=5:
                # ~ print("No motion from sensor 2, reactivating sensor1, FALSE ALARM")    
                # ~ #pir1 = MotionSensor(18)
        # ~ #if motion5s == True:
            # ~ #print ("Motion was detected in last 5 seconds, was detected %0.10f " %(motionseconds) + " ago.")
        # ~ #elif motion5s == False:
            # ~ #print ("No motion detected within last 5 seconds, was detected %0.10f " %(motionseconds) + " ago.")
            # ~ time.sleep(0.25)           #quaarter second delay    

#pir1.when_motion = lambda: motion_function("1")

#activeMode=int(input("Please choose a mode (1-3): "))
#if activeMode==1:

def mode1():
 #   while True:
    #pir1.when_motion = lambda: going_direction("1")
    #pir2.when_motion = lambda: going_direction("2")
    while True:
        pir1.wait_for_motion() #= lambda: going_direction("1")
        going_direction(1)
        pir2.when_motion # = lambda: going_direction("2")
        going_direction(2)
        #pir1.wait_for_motion = going_in




def modeTwo():
    while True:
        sense.show_message("ALARM ON!")
        if (pir1.motion_detected == True or pir2.motion_detected == True):
            sense.show_message("INTRUDER!!!")
            while True:
                answer = input("Please enter password to desactivate alarm: ")
                if answer == password:
                    print("Alarm desactivated, back to alarm mode")
                    break
                else:
                    print("Wrong password, alarm still beeping")
            sense.show_message("ALARM ON!")

import time
from datetime import datetime
import random
import string
import keyboard # only to simulate sensor, can delete later

# mode one - room reservation mode
# For now, to check it make sure to select a start time before or equal to current hour and end time after current hour
# Can select hour that already passed
# To implement later : days, and error if selecting passed hour



def password_generator(): # basic password generator function, only lower case letters, can adjust lentgh
    length = 5
    letters = string.ascii_lowercase
    result_pw = ''.join(random.choice(letters) for i in range(length))
    return result_pw        

def mode_one(): # Function one to reserve room
    details=0 # variable used to check if user name/pw are correct
    room_occupied = 0

    motion_last_detected = 0 # counter to check when the person was last in room
    max_time_out_of_room = 5 # adjust time (in seconds for test, for real use probably minutes) a person cna be outside the room while its reserved

    print("\nWelcome to the room reservation system")
    name=input("\nEnter your name: ")
    start_time = int(input("\nEnter the start time of the reservation (8-19): "))
    end_time = int(input(f"\nEnter the end time of the reservation ({start_time+1}-20): "))
    password = password_generator()
    print(f"\nYour name is {name}, your password will be '{password}', your reservation starts at {start_time} and ends at {end_time}. Work hard!")
    
    print("\n")

    print_status = True # Boolean variable to be able to print only once when in While loops

    while True:
        hour=(time.localtime()).tm_hour # get the local time hour
        time.sleep(0.05) # avoid permanent loop, was causing issues with the keyboard.is_pressed method

        if (hour>=start_time and hour<end_time): # check time compared to reservation
  
            if keyboard.is_pressed("x"): # press x = sensor 1 outside is activated 
                
                while details==0: # as long as name/pwd incorrect, loop
                    answer_name = input("\nWelcome visitor. Enter your name: ")
                    answer_password = input("Enter your password: ")

                    if (answer_name==name and answer_password==password):
                        print(f"\nWelcome {name} to your room!")
                        details=1
                        room_occupied=1
                        print_status = True

                        while True: # loop for detecting going outside, person already in room
                        
                            if keyboard.is_pressed("y"):
                                
                                print(f"\nYou exited the room! If you're not back within {max_time_out_of_room} seconds, your reservation will freed up.")                           
                                print_status = True
                                time_out = time.time()

                                while motion_last_detected < max_time_out_of_room: # loop while the person is outside
                                    motion_last_detected = time.time() - time_out
                                    #print(motion_last_detected)
                                
                                    if keyboard.is_pressed("x"): # if motion detected outside (sensor 1)
                                        
                                        print(f"\nWelcome back {name}!")
                                        print_status = True
                                        break

                                    elif print_status:
                                        print("\nAwaiting return... ( press 'x' to simulate motion sensor 1)")
                                        print_status=False

                                if motion_last_detected < max_time_out_of_room: # if the person came back before timer, goes back to loop while inside the room
                                    continue

                                else: # if person out too long, game over
                                    print("\nYou took too long to come back! Your reservation is now cancelled.")
                                    exit()

                            elif print_status:
                                print(f"\n{name} still in room... (press 'y' to exit room (simulate Motion sensor2))")
                                print_status=False
                    else:
                        print("Name and/or password inccorect. Try again") 

            elif print_status:
                
                print(f"\nWaiting for {name} to show up...")
                print("To simulate motion sensor: press 'x' to detect Motion 1(outside) and 'y' to detect motion 2 (inside)")
                print_status=False         

        elif print_status: # if hour is not yet reached start time
            print(f"\nNo reservation at {hour}. Next reservation at {start_time}")   
            print_status=False       


mode_one()

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

    
