from gpiozero import LED, MotionSensor
import time
from datetime import datetime
from signal import pause
from sense_hat import SenseHat
from animate import *
import threading

sense = SenseHat()

status1 = 0     #sensor 1 status
status2 = 0     #-||- 2

pir1= MotionSensor(pin=18,threshold=0.2)
pir2 = MotionSensor(pin=17,threshold=0.2)

def mode1():
 
    t1 = threading.Thread(target=mode1a)   #One thread is assigned to the mode1a() function (using target=)
    t2 = threading.Thread(target=mode1b)   #ditto for mode1b()    
    
    t1.start()  #the threads start running their defined functions in the background.
    t2.start()
        
                #the main loop continues running here.
    while True:
                #the main loop examines two global variables that are controlled by the sensor threads in order to determine what's happening.
        if status1 > status2 and status2 > 0:  
            dirTimer = 150
            movementBoth()                                  #this function is from animate.py which shows a specific image from graphics.py
            while dirTimer >= 0:
                print("GOING OUT: status1 =",status1," and status2 =",status2)
                if status1 == 0 and status2 > 0:
                    movementOut()
                    time.sleep(1.2)      
                    break                                
                elif status1 > 0 and status2 == 0:   
                    break
                dirTimer = dirTimer - 1
                time.sleep(0.01)
            
        elif status2 > status1 and status1 > 0:
            dirTimer = 150
            movementBoth()
            while dirTimer >= 0:
                print("GOING IN status1 =",status1," and status2 =",status2)
                if status2 == 0 and status1 > 0:
                    movementIn()
                    time.sleep(1.2)      
                    break                                #this function is from animate.py which shows a specific image from graphics.py
                elif status2 > 0 and status1 == 0:   
                    break
                dirTimer = dirTimer - 1
                time.sleep(0.01)
                
        elif status1 != 0 and status2 == 0:         #movement detected only from the left.
            movementLeft()
            
        elif status1 == 0 and status2 != 0: 
            movementRight()
            
        else:
            sense.clear()
        time.sleep(0.1)


def mode1a():   #Thread t1 starts here.
    
    global status1
    sensorTimer1 = 0
    
    while True: 
        if pir1.motion_detected:
            if status2 == 0:        #if the other sensor hasn't detected anything recently, this sensor gets the higher status (and vice versa)
                status1 = 2
            else:
                status1 = 1
            sensorTimer1 = 150
            pir1.wait_for_no_motion()
        
        if sensorTimer1 > 0:
            sensorTimer1 = sensorTimer1 - 1
        if sensorTimer1 == 0 and status1 > 0:
            status1 = 0
        time.sleep(0.02)
        

def mode1b():   #...and thread t2 starts here.
    
    global status2
    sensorTimer2 = 0

    while True:
        
        if pir2.motion_detected:
            if status1 == 0:
                status2 = 2
            else:
                status2 = 1
            sensorTimer2 = 150
            pir2.wait_for_no_motion()
             
             
        if sensorTimer2 > 0:
            sensorTimer2 = sensorTimer2 - 1
        if sensorTimer2 == 0 and status2 > 0:
            status2 = 0
        time.sleep(0.02)








###outdated modes


def modeTwo():
    while True:
        sense.show_message("ALARM ON!")
        if (pir1.motion_detected == True or pir2.motion_detected == True):
            sense.show_message("INTRUDER!!!", text_colour=red)
            while True:
                answer = input("Please enter password to deactivate alarm: ")
                if answer == password:
                    print("Alarm deactivated, back to alarm mode")
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
        
