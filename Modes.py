from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
from sense_hat import SenseHat

sense = SenseHat()
#sense.set_rotation(180)

lastmotion = 0
motion5s = 0


countdown = 5

pir1= MotionSensor(18)
pir2 = MotionSensor(17)

password = "abc123"

blue = (0,0,255)
green = (0, 255, 0)
red = (255, 0, 0) 
yellow = (255,255,0)
black = (0,0,0)


X = yellow
O = black  

smiley_face = [
O, O, O, O, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, X, O, X, O, O, O,
O, O, X, O, X, O, O, O,
X, O, O, O, O, O, X, O,
O, X, O, O, O, X, O, O,
O, O, X, X, X, O, O, O,
O, O, O, O, O, O, O, O
]



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
            #print(motionseconds)
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
            sense.show_message("INTRUDER!!!", text_colour=red)
            while True:
                answer = input("Please enter password to desactivate alarm: ")
                if answer == password:
                    print("Alarm desactivated, back to alarm mode")
                    break
                else:
                    print("Wrong password, alarm still beeping")
            sense.show_message("ALARM ON!")


def modeThree():
    count=countdown
    while count>0:
        sense.show_message(str(count), text_colour=blue)
        time.sleep(1)
        count-=1
        if (pir1.motion_detected == True or pir2.motion_detected == True):
            print("Motion detected, reseting countdown")
            count = countdown
    print("\nNO MOTION DETECTED, CHECK UP REQUIRED!!")
    while True:
        sense.show_message("ALERT", text_colour=red)
        i = input("Enter 'exit' to desactivate alarm: ")
        if i=="exit":
            break
        else:
            print("Command not recognized, alarm ON")
        #print("Your input:", i)
    print("Alarm desactivated ")
    sense.set_pixels(smiley_face)
    time.sleep(3)
    sense.clear()
        
