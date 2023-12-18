
from datetime import datetime
from datetime import timedelta
import random
import string
from gpiozero import LED, MotionSensor
import keyboard # Used to simulate sensors in testings without raspberry pi AND to exit modes at any time, not to delete. May cause errors
from clockdisplay_minute_second import *
import threading
from graphics import *
from animate import *

class Cancelled(Exception): pass

#sense = SenseHat()

pir1= MotionSensor(18) #inside sensor
pir2 = MotionSensor(17) #outside sensor
sense.clear()

green = (0, 255, 0)
red = (255, 0, 0)

status1 = 0     #sensor 1 status
status2 = 0     #-||- 2

global alive_status
alive_status = 0

# mode one - room reservation mode
# For now, to check it make sure to select a start time before or equal to current hour and end time after current hour
# Can select hour that already passed
# To implement later : days, and error if selecting passed hour when reserving. Add counter for another person enter the room then make sure room is empty at the end.


# mode two - Alarm mode
# When going to work, going on holidays etc... and house is empty. Activate alarm until desired date. For now only same day for testing purposes, easily modifiable.
# once motion is detected -> alarm beeps. need to answer password to desactivate alarm


# mode three - monitoring mode (ex: retirement homes)
# check if any motion at all during the amount of hours selected. Can also be modified later


# creation of quick method prRed to print in red in terminal
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

#password used for mode two
password = "abc123"
#out_of_room_before_timer = 0 # used for function within mode 1. Need to improve


def clear_sensor():
    pass

def welcome_back(name):
    print(f"\nWelcome back {name}!")
    print_status = True
    global out_of_room_before_timer
    out_of_room_before_timer = 1
    

def password_generator(): # basic password generator function, only lower case letters, can adjust lentgh. Used for mode one
    length = 5
    letters = string.ascii_lowercase
    result_pw = ''.join(random.choice(letters) for i in range(length))
    return result_pw        

def mode_one(): # Function one to reserve room
    
    sensorThread1 = threading.Thread(target=sensor1Loop)   #One thread is assigned to a function (using target=function)
    sensorThread2 = threading.Thread(target=sensor2Loop)   
    
    sensorThread1.start()  #the threads start running their defined functions in the background.
    sensorThread2.start()
    global status1
    global status2
    personCount = 0
    time_out = 0
    
    print_status = True # Boolean variable to be able to print only once when in While loops  
    out_of_room_before_timer = 0  
    #details=0 # variable used to check if user name/pw are correct
    #room_occupied = 0

    motion_last_detected = 0 # counter to check when the person was last in room
    max_time_out_of_room = 10 # adjust time (in seconds for test, for real use probably minutes) a person cna be outside the room while its reserved

    print("\nWelcome to the room reservation system")
    name=input("\nEnter your name: ")
    start_time = int(input("\nEnter the start time of the reservation (8-19): "))
    end_time = int(input(f"\nEnter the end time of the reservation ({start_time+1}-20): "))
    password = password_generator()
    print(f"\nYour name is {name}, your password will be '{password}', your reservation starts at {start_time} and ends at {end_time}. Work hard!")
    
    print("\n")


    while True:
        hour=(time.localtime()).tm_hour # get the local time hour
        #time.sleep(0.05) # avoid permanent loop, was causing issues with the keyboard.is_pressed method
        try:
            if (hour>=start_time and hour<end_time): # check time compared to reservation
                
                    
                print(f"\nWaiting for 'someone' to show up...")
                #sense.show_message("Varattu")
                print_status=False  
      
                while status2 == 0:
                    time.sleep(0.1)
                        # wait for sensor 2 outside to be activated 
                answer_name = input("\nWelcome visitor. Enter your name: ")
                answer_password = input("Enter your password: ")
                print("ID")
                sense.show_message("ID")
                    
                while (answer_name!=name or answer_password!=password): # as long as name/pwd incorrect, loop
                    print("Name and/or password inccorect. Try again") 
                    answer_name = input("\nWelcome visitor. Enter your name: ")
                    answer_password = input("Enter your password: ")
                    print("ID")
                    sense.show_message("ID")

                if (answer_name==name and answer_password==password):
                    print(f"\nWelcome {name} to your room!")

                        #details=1
                        #room_occupied=1
                    print_status = True

                    print(f"\n{name} is in the room... (awaiting Motion sensor1))")
                        #sense.show_message("VARATTU")
                    print_status=False
                    
                    personCount = personCount + 1
                    status1 == 0
                    status2 == 0
                    print("Sisällä on ",personCount," henkilöä.")
                    while True:
                #the main loop examines two global variables that are controlled by the sensor threads in order to determine what's happening.
                        if status1 > status2 and status2 > 0:  
                            dirTimer = 150
                            movementBoth()                                  #this function is from animate.py which shows a specific image from graphics.py
                            while dirTimer >= 0:

                                if status1 == 0 and status2 > 0:
                                    movementOut()
                                    if personCount > 0:
                                        personCount = personCount - 1
                                    if personCount == 0:
                                        prRed(f"\nNo-one left in the room! If you're not back within {max_time_out_of_room} seconds, your reservation will freed up.")                         
                                        print_status = True
                                        time_out = time.time()    
                                    
                                    print("Sisällä on ",personCount," henkilöä.")
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
                                if status2 == 0 and status1 > 0:
                                    movementIn()
                                    personCount = personCount + 1
                                    print("Sisällä on ",personCount," henkilöä.")
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
                            if personCount > 0:
                                sense.show_letter(str(personCount),green)
                            else:
                                sense.show_letter(str(personCount),red)
                            
                        if personCount == 0 and (time.time() - time_out) > max_time_out_of_room:
                            raise Cancelled
                        time.sleep(0.02)
                        
                    
        except Cancelled:
            prRed(f"\nYou took too long to come back{name}! Your reservation is now cancelled.\nPress e to go back to menu")


        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nMode ROOM booking exited successfully")
            sense.clear()
            break

        elif print_status: # if hour is not yet reached start time
            print(f"\nNo reservation at {hour}. Next reservation at {start_time}") 
            sense.clear()
            #sense.show_message("VAPAA")  
            print_status=False       


def sensor1Loop():
    global status1
    global status2
    
    while True: 
        if pir1.motion_detected:
            if status2 == 0:        #if the other sensor hasn't detected anything recently, this sensor gets the higher status (and vice versa)
                status1 = 2
            else:
                status1 = 1
            time.sleep(1.8)
            status1 = 0
        time.sleep(0.01)
        
    
def sensor2Loop():
    global status1
    global status2

    while True:
        
        if pir2.motion_detected:
            if status1 == 0:
                status2 = 2
            else:
                status2 = 1
            time.sleep(1.8)
            status2 = 0
        time.sleep(0.01)
        
        
def alarm_on():
    prRed("INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER")
    sense.show_letter("!", text_colour=red)
    answer=input("Please enter password to desactivate alarm: ")
    while answer!=password:
        print("Wrong password, alarm still beeping") 
        answer=input("Please enter password to desactivate alarm: ")
    print("Alarm desactivated, back to alarm mode")
    print("\nALARM MODE ON")
    sense.show_letter("O", text_colour=green)


def mode_two():
    print_status = True # Boolean variable to be able to print only once when in while loops
    countdown_reached = 1 # variable to differentiate if timer reached or mode exited before end of timer
    print("\nUntil when should the ALARM be ON?: ") # user input to choose times, ints
    #year_user = int(input("year: "))
    #month_user = int(input("month: "))
    #day_user = int(input("day: "))    
    hour_user = int(input("hour: "))
    minute_user = int(input("minutes: "))

    year = datetime.now().year # for testing purposes, fetch the current year month and day
    month = datetime.now().month
    day = datetime.now().day

    countdown_to = datetime(year,month,day,hour_user,minute_user) # countdown variable until the selected time
    print("\nAlarm iniated at", datetime.now(), "until", countdown_to, "\n")

    while datetime.now() < countdown_to: # loop through time until countdown reached
        if print_status:
            print("ALARM MODE ON")
            sense.show_letter("O", text_colour=green)
            print_status=False
        pir2.when_motion = alarm_on
        pir1.when_motion = alarm_on#or pir2.motion_detected == True): 
        # ~ prRed("INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER")
        # ~ sense.show_letter("!", text_colour=red)
        # ~ answer=input("Please enter password to desactivate alarm: ")
        # ~ while answer!=password:
            # ~ print("Wrong password, alarm still beeping") 
            # ~ answer=input("Please enter password to desactivate alarm: ")
        
        # ~ print("Alarm desactivated, back to alarm mode")
        # ~ print_status=True
            # ~ while True: # loop to turn off alarm
                # ~ #sense.show_message("INTRUDER", text_colour=red)
                # ~ sense.show_letter("!", text_colour=red)
                # ~ answer=input("Please enter password to desactivate alarm: ")
                # ~ if answer == password:
                    # ~ print("Alarm desactivated, back to alarm mode")
                    # ~ sense.show_letter("O")  
                    # ~ #(pir1.motion_detected == True or pir2.motion_detected == True)
                    # ~ break
                # ~ if answer == 'e':
                    # ~ sense.clear()
                    # ~ break
                # ~ else:
                    # ~ print("Wrong password, alarm still beeping")          
        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nMode ALARM exited successfully")
            countdown_reached = 0
            sense.clear()
            break
    if countdown_reached == 1:
        print("Timer reached, ALARM OFF. Back to menu")
        sense.show_letter("O", text_colour=red)
        pir2.when_motion = clear_sensor
        pir1.when_motion = clear_sensor
        time.sleep(2)
    #break
    if countdown_reached==0:
        print("Back to menu")
        pir2.when_motion = clear_sensor
        pir1.when_motion = clear_sensor
    #break
        # ~ elif print_status:
            # ~ print("ALARM MODE ON")
            # ~ #sense.show_letter("O")
            # ~ print_status=False


def everybody_alive():
    print("\nMotion detected, everybody alive!")
    smiley()
    alive_status=1


def mode_three():
    print_status=True
    alive_status=0 # variable in case timer reach 0 without motion -> alarm
    B = 0  # workaround to print only once in the countdown loop, otherwise print many times due to too good precision of seconds
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute

    #print("\nHow long shoud the MONITORING be ON?: ")
    #hour_user = int(input("Hours: "))
    #if hour_user+hour>23: # if else to solve the +24hours problem
    #    hour_new = hour+hour_user-24
    #    day = day+1
    #    countdown_to = datetime(year,month,day,hour_new,minutes)
    #else:
    #    countdown_to = datetime(year,month,day,hour+hour_user,minutes)

    countdown_to = datetime(year,month,day,hour,minute+1) # testing countdown (time+1minute)
    print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")


    while (datetime.now() < countdown_to and pir2.motion_detected==False):
        time.sleep(0.01)
        
        countdown = int((countdown_to - datetime.now()).total_seconds())
        
        if countdown%10 == 0 and B!=countdown: #countdown every 10 seconds, useful for quick testing, no need to wait one minute
        #if datetime.now().minute != last_minute: #countdown every minute
            time_left_seconds = int((countdown_to - datetime.now()).total_seconds())
            time_converted = str(timedelta(seconds=time_left_seconds))
            print('Time left:', time_converted)
            #print('Time left:', int((countdown_to - datetime.now()).total_seconds() // 60), 'min') # if the countdown is in minute
            print('Time now:', datetime.now(), '\n')
            B=countdown           
            #last_minute = datetime.now().minute # if countdown in minutes 

    if pir2.motion_detected==True:
        
        print("\nMotion detected, everybody alive!")
        smiley()
        alive_status=1
            # ~ answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
            # ~ if answer=="y":
                # ~ hour_plus_twelve=datetime.now().hour+12
                # ~ if hour_plus_twelve>23:
                    # ~ hour_new = hour_plus_twelve-24
                    # ~ day = datetime.now().day+1
                    # ~ countdown_to = datetime(year,month,day,hour_new,minute)
                # ~ else:
                    # ~ countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                # ~ print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                # ~ continue
            # ~ elif answer=="n":
                # ~ print("\nExiting MONITORING MODE")
                # ~ break

        # ~ if keyboard.is_pressed("e"):
            # ~ print("Mode exited, back to menu") 
            # ~ alive_status=2
            # ~ break

        # ~ elif print_status:
           # ~ print("(Press x or y to simulate sensors), e to exit")
           # ~ print_status=False

   # if alive_status == 1:
       # print("Motion detected, everybody alive! Monitoring OFF") 
   # if alive_status == 2:
        #print("Mode exited, back to menu")          
    if alive_status==0:  
        prRed("ALERT, time reached without motion. SEND HELP") 
        dead()
    time.sleep(2)    


# ~ def mode_three():
    # ~ print_status=True
    # ~ alive_status=0 # variable in case timer reach 0 without motion -> alarm
    # ~ B = 0  # workaround to print only once in the countdown loop, otherwise print many times due to too good precision of seconds
    # ~ year = datetime.now().year
    # ~ month = datetime.now().month
    # ~ day = datetime.now().day
    # ~ hour = datetime.now().hour
    # ~ minute = datetime.now().minute
    # ~ last_second = (datetime.now().second)-2
    # ~ #print("\nHow long shoud the MONITORING be ON?: ")
    # ~ #hour_user = int(input("Hours: "))
    # ~ #if hour_user+hour>23: # if else to solve the +24hours problem
    # ~ #    hour_new = hour+hour_user-24
    # ~ #    day = day+1
    # ~ #    countdown_to = datetime(year,month,day,hour_new,minutes)
    # ~ #else:
    # ~ #    countdown_to = datetime(year,month,day,hour+hour_user,minutes)

    # ~ #countdown_to = datetime(year,month,day,hour,minute+2) # !!! TESTING !!! countdown (time+2minute) take bloc above for real use
    # ~ #print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
    # ~ print(pir2.motion_detected)
    # ~ #print(last_second)
    # ~ while (datetime.now().second!=last_second and pir2.motion_detected==False):
        # ~ print(last_second)
        # ~ last_second=datetime.now().second
        # ~ #time.sleep(1)
    # ~ print("\nMotion detected, everybody alive!")
        

    # ~ while datetime.now() < countdown_to:
        
        # ~ countdown = int((countdown_to - datetime.now()).total_seconds())
        # ~ time_left_seconds = countdown - 1
        
        # ~ #if countdown%10 == 0 and B!=countdown: #countdown every 10 seconds, useful for quick testing, no need to wait one minute
        # ~ if countdown!=time_left_seconds:
        # ~ #if datetime.now().minute != last_minute: #countdown every minute
            # ~ time_left_seconds = int((countdown_to - datetime.now()).total_seconds())
            # ~ time_converted = str(timedelta(seconds=time_left_seconds))
            # ~ print(int(countdown/60))
            # ~ print(countdown%60)
            # ~ display_time(int(countdown)/60, countdown%60)
            # ~ print('Time left:', time_converted)
            # ~ #print('Time left:', int((countdown_to - datetime.now()).total_seconds() // 60), 'min') # if the countdown is in minute
            # ~ print('Time now:', datetime.now(), '\n')
            # ~ B=countdown           
            # ~ #last_minute = datetime.now().minute # if countdown in minutes 

            # ~ pir2.wait_for_motion() #or pir2.motion_detected == True):
            # ~ print("\nMotion detected, everybody alive!")
            # ~ sense.set_pixels(smiley_face)
            # ~ alive_status=1
            # ~ answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
            # ~ if answer=="y":
                # ~ hour_plus_twelve=datetime.now().hour+12
                # ~ if hour_plus_twelve>23:
                    # ~ hour_new = hour_plus_twelve-24
                    # ~ day = datetime.now().day+1
                    # ~ countdown_to = datetime(year,month,day,hour_new,minute)
                # ~ else:
                    # ~ countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                # ~ print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                # ~ break
            # ~ elif answer=="n":
                # ~ sense.clear()
                # ~ break
            # ~ pir2.when_motion = everybody_alive  
            # ~ print(alive_status)
            # ~ if alive_status==0:
                # ~ pass
            # ~ elif alive_status==1:
                # ~ answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
                # ~ if answer=="y":
                    # ~ hour_plus_twelve=datetime.now().hour+12
                    # ~ if hour_plus_twelve>23:
                        # ~ hour_new = hour_plus_twelve-24
                        # ~ day = datetime.now().day+1
                        # ~ countdown_to = datetime(year,month,day,hour_new,minute)
                    # ~ else:
                        # ~ countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                    # ~ print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                    # ~ continue
                # ~ elif answer=="n":
                    # ~ print("\nExiting MONITORING MODE")
                    # ~ break
                    # ~ sense.clear()
        # ~ #sense.clear()
        # ~ #break 
    
            
        # ~ #if answer=="y":
         # ~ #   continue
        # ~ #if answer=="n":
         # ~ #   print("\nExiting MONITORING MODE")
          # ~ #  break
        # ~ #if keyboard.is_pressed("e"):
        # ~ #    print("Mode exited, back to menu") 
        # ~ #    sense.clear()
        # ~ #    alive_status=2
        # ~ #    break

        # ~ elif print_status:
           # ~ #print("(Press x or y to simulate sensors), e to exit")
           # ~ print_status=False

   # ~ # if alive_status == 1:
       # ~ # print("Motion detected, everybody alive! Monitoring OFF") 
   # ~ # if alive_status == 2:
        # ~ #print("Mode exited, back to menu")          
    # ~ if alive_status==0:  
        # ~ prRed("ALERT, time reached without motion. SEND HELP") 
        # ~ sense.show_message("ALERT", text_colour=red)
    # ~ time.sleep(2)    
    
    # ~ while datetime.now() < countdown_to:
        
        # ~ countdown = int((countdown_to - datetime.now()).total_seconds())
        
        # ~ if countdown%10 == 0 and B!=countdown: #countdown every 10 seconds, useful for quick testing, no need to wait one minute
        # ~ #if datetime.now().minute != last_minute: #countdown every minute
            # ~ time_left_seconds = int((countdown_to - datetime.now()).total_seconds())
            # ~ time_converted = str(timedelta(seconds=time_left_seconds))
            # ~ print('Time left:', time_converted)
            # ~ #print('Time left:', int((countdown_to - datetime.now()).total_seconds() // 60), 'min') # if the countdown is in minute
            # ~ print('Time now:', datetime.now(), '\n')
            # ~ B=countdown           
            # ~ #last_minute = datetime.now().minute # if countdown in minutes 

        # ~ if pir2.motion_detected==True:

            # ~ print("\nMotion detected, everybody alive!")
            # ~ alive_status=1
            # ~ answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
            # ~ if answer=="y":
                # ~ hour_plus_twelve=datetime.now().hour+12
                # ~ if hour_plus_twelve>23:
                    # ~ hour_new = hour_plus_twelve-24
                    # ~ day = datetime.now().day+1
                    # ~ countdown_to = datetime(year,month,day,hour_new,minute)
                # ~ else:
                    # ~ countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                # ~ print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                # ~ continue
            # ~ elif answer=="n":
                # ~ print("\nExiting MONITORING MODE")
                # ~ break

        # ~ if keyboard.is_pressed("e"):
            # ~ print("Mode exited, back to menu") 
            # ~ alive_status=2
            # ~ break

        # ~ elif print_status:
           # ~ print("waiting for motion")
           # ~ print_status=False
        
    # ~ if alive_status==0:  
        # ~ prRed("ALERT, time reached without motion. SEND HELP") 
    # ~ time.sleep(2)  
    
    # ~ while (datetime.now() < countdown_to and pir2.motion_detected==False):
        
        # ~ countdown = int((countdown_to - datetime.now()).total_seconds())
        
        # ~ if (countdown%10 == 0 and B!=countdown): #countdown every 10 seconds, useful for quick testing, no need to wait one minute
        # ~ #if datetime.now().minute != last_minute: #countdown every minute
            # ~ time_left_seconds = int((countdown_to - datetime.now()).total_seconds())
            # ~ time_converted = str(timedelta(seconds=time_left_seconds))
            # ~ print('Time left:', time_converted)
            # ~ #print('Time left:', int((countdown_to - datetime.now()).total_seconds() // 60), 'min') # if the countdown is in minute
            # ~ print('Time now:', datetime.now(), '\n')
            # ~ B=countdown           
            # ~ #last_minute = datetime.now().minute # if countdown in minutes 


    # ~ print("\nMotion detected, everybody alive!")
    # ~ alive_status=1
    # ~ answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
    # ~ if answer=="y":
    # ~ hour_plus_twelve=datetime.now().hour+12
    # ~ if hour_plus_twelve>23:
        # ~ hour_new = hour_plus_twelve-24
                    # ~ day = datetime.now().day+1
                    # ~ countdown_to = datetime(year,month,day,hour_new,minute)
                # ~ else:
                    # ~ countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                # ~ print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                # ~ continue
            # ~ elif answer=="n":
                # ~ print("\nExiting MONITORING MODE")
                # ~ break

        # ~ if keyboard.is_pressed("e"):
            # ~ print("Mode exited, back to menu") 
            # ~ alive_status=2
            # ~ break

        # ~ elif print_status:
           # ~ print("waiting for motion")
           # ~ print_status=False
        
    # ~ if alive_status==0:  
        # ~ prRed("ALERT, time reached without motion. SEND HELP") 
    # ~ time.sleep(2)  

""" def mode_three():
    countdown=int(input("Time without motion before alarm goes off (seconds): "))
    count=countdown
    print_status=True
    while count>0:
        prRed(str(count))
        time.sleep(1)
        count-=1
        if keyboard.is_pressed("y") or keyboard.is_pressed("x"):
            print("Motion detected, reseting countdown")
            print_status=True
            count = countdown
        elif print_status:
            print("Press x or y to simulate sensors")
            print_status=False

    prRed("\nALARM, NO MOTION DETECTED, CHECK UP REQUIRED!!")       
    while True:
        prRed("ALERT")
        i = input("Enter 'off' to desactivate alarm: ")
        if i=="off":
            break
        else:
            print("Command not recognized, alarm going on")
        #print("Your input:", i)
    print("Alarm desactivated ")
    time.sleep(3) """

""" def modeThree():
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
         """
""" def modeTwo2():
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
 """





def mode_four():
    
    personCount = 0
    t1 = threading.Thread(target=mode4a)   #One thread is assigned to the mode1a() function (using target=)
    t2 = threading.Thread(target=mode4b)   #ditto for mode1b()    
    
    t1.start()  #the threads start running their defined functions in the background.
    t2.start()
        
                #the MAIN loop continues running here.
    while True:
                #the main loop examines two global variables that are controlled by the sensor threads in order to determine what's happening.
        if status1 > status2 and status2 > 0:  
            dirTimer = 150
            movementBoth()                                  #this function is from animate.py which shows a specific image from graphics.py
            while dirTimer >= 0:

                if status1 == 0 and status2 > 0:
                    movementOut()
                    if personCount > 0:
                        personCount = personCount - 1
                    print("Sisällä on ",personCount," henkilöä.")
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

                if status2 == 0 and status1 > 0:
                    movementIn()
                    personCount = personCount + 1
                    print("Sisällä on ",personCount," henkilöä.")
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
        time.sleep(0.02)


def mode4a():   #Thread t1 starts here.
    
    global status1
    sensorTimer1 = 0
    
    while True: 
        if pir1.motion_detected:
            if status2 == 0:        #if the other sensor hasn't detected anything recently, this sensor gets the higher status (and vice versa)
                status1 = 2
            else:
                status1 = 1
            sensorTimer1 = 120
            pir1.wait_for_no_motion()
        
        if sensorTimer1 > 0:
            sensorTimer1 = sensorTimer1 - 1
        if sensorTimer1 == 0 and status1 > 0:
            status1 = 0
        time.sleep(0.01)
        

def mode4b():   #...and thread t2 starts here.
    
    global status2
    sensorTimer2 = 0

    while True:
        
        if pir2.motion_detected:
            if status1 == 0:
                status2 = 2
            else:
                status2 = 1
            sensorTimer2 = 120
            pir2.wait_for_no_motion()
             
             
        if sensorTimer2 > 0:
            sensorTimer2 = sensorTimer2 - 1
        if sensorTimer2 == 0 and status2 > 0:
            status2 = 0
        time.sleep(0.01)
