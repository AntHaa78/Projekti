
from datetime import datetime
from datetime import timedelta
import random
import string
from gpiozero import LED, MotionSensor
import keyboard # Used to simulate sensors in testings without raspberry pi. Now to to exit modes at any time ('e')
from clockdisplay_minute_second import *
import threading
from graphics import *
from animate import *

class Cancelled(Exception): pass


pir1= MotionSensor(18) #inside sensor
pir2 = MotionSensor(17) #outside sensor
sense.clear()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

status1 = 0     #sensor 1 status
status2 = 0     #-||- 2

# mode one - room reservation mode


# mode two - Alarm mode
# When going to work, going on holidays etc... and house is empty. Activate alarm until desired date. For now only same day for testing purposes, easily modifiable.
# once motion is detected -> alarm beeps. need to answer password to desactivate alarm


# mode three - monitoring mode (ex: retirement homes)
# check if any motion at all during the amount of hours selected. Can also be modified later


# creation of quick method prRed to print in red in terminal, prGreen green 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

#password used for mode two
password = "abc123"


def back_to_menu():
    print("Exiting current mode. Going back to menu")

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

def mode_one(): # Function one to reserve room. Need to implement calendar/more dates choice later. Currently only current month
    
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
    max_time_out_of_room = 10 # adjust time (in seconds for test, for real use probably minutes) a person can be outside the room while its reserved

    print("\nWelcome to the room reservation system for December")
    name=input("\nEnter your name: ")
    hour=(time.localtime()).tm_hour
    day=(time.localtime())[2]
    
    day_user=int(input(f"\nEnter the day of the reservation ({day}-31): "))
    if day_user==day:
        start_time = int(input(f"\nEnter the start time of the reservation ({hour}-19): "))
    else:
        start_time = int(input(f"\nEnter the start time of the reservation (8-19): "))
    end_time = int(input(f"\nEnter the end time of the reservation ({start_time+1}-20): "))
    password = password_generator()
    if (hour>=start_time and hour<end_time and day_user==day):
        print(f"\nYour name is {name}, your password will be '{password}', your reservation starts at {start_time} and ends at {end_time}. Work hard!")
    else:
        pass
    print("\n")


    while True:
         
        #time.sleep(0.05) # to avoid permanent loop, was causing issues with the keyboard.is_pressed method
        try:
            if (hour>=start_time and hour<end_time and day_user==day): # check time compared to reservation
                
                    
                print(f"\nWaiting for 'someone' to show up...")
                
                print_status=False  
      
                while status2 == 0:
                    time.sleep(0.1)
                        # wait for sensor 2 outside to be activated 
                answer_name = input("\nWelcome visitor. Enter your name: ")
                answer_password = input("Enter your password: ")
                print("ID check...")
                sense.show_message("ID")
                    
                while (answer_name!=name or answer_password!=password): # as long as name/pwd incorrect, loop
                    print("Name and/or password inccorect. Try again") 
                    answer_name = input("\nWelcome visitor. Enter your name: ")
                    answer_password = input("Enter your password: ")
                    print("ID check...")
                    sense.show_message("ID")

                if (answer_name==name and answer_password==password):
                    print(f"\nWelcome {name} to your room booked!")
                    max_time_out_of_room = int(input("How long before the reservation cancels if the room is empty? (max 15 secs, default=10)"))
               
                    print_status = True

                    print(f"\n{name} is in the room... ")
                        
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
            prRed(f"\nYou took too long to come back {name}! Your reservation is now cancelled.")
            break


        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nMode ROOM booking exited successfully")
            sense.clear()
            break

        elif print_status: # if hour is not yet reached start time
            print(f"\nNo reservation at {hour} on {day}/12. Next reservation at {start_time} on {day_user}/12") 
            sense.clear()
            
            print_status=False   
            break    


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
    print("Alarm desactivated.")
    print("\nALARM MODE ON")
    sense.show_letter("O", text_colour=green)


def mode_two():
    print_status = True # Boolean variable to be able to print only once when in while loops
    countdown_reached = 1 # variable to differentiate if timer reached or mode exited before end of timer (forceful exit or alarm desactivated)
    print("\nUntil when should the ALARM be ON?: ") # user input to choose times, ints
    #year_user = int(input("year: "))
    #month_user = int(input("month: "))
    #day_user = int(input("day: "))    
    hour_user = int(input("hour: "))
    minute_user = int(input("minutes: "))

    year = datetime.now().year # for testing purposes, fetch the current year month and day
    month = datetime.now().month
    day = datetime.now().day

    end_time = datetime(year,month,day,hour_user,minute_user) # End time for alarm
    print("\nAlarm iniated at", datetime.now(), "until", end_time, ". Press 'e' to exit at any time\n")

    while datetime.now() < end_time: # loop through time until countdown reached
        if print_status:
            print("ALARM MODE ON")
            sense.show_letter("O", text_colour=green)
            print_status=False

        pir2.when_motion = alarm_on
        pir1.when_motion = alarm_on
                
        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nALARM DESACTIVATED.")
            countdown_reached = 0
            sense.clear()
            break
    if countdown_reached == 1:
        print("Timer reached, ALARM OFF.")
        sense.show_letter("O", text_colour=red)
        pir2.when_motion = clear_sensor
        pir1.when_motion = clear_sensor
        time.sleep(2)
    
    if countdown_reached==0:
        #print("Back to menu")
        pir2.when_motion = clear_sensor
        pir1.when_motion = clear_sensor


def mode_three():
    
    alive_status=0 # variable in case timer reach 0 without motion -> alarm
    B = 0  # workaround to print only once in the countdown loop, otherwise print many times due to too good precision of seconds
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute

	# Code of block for user to choose himself lentgh of alarm, instead of the +2 minute in testings.
    #print("\nHow long shoud the MONITORING be going before alarm (max 24h)?: ")
    #hour_user = int(input("Hours: "))
    #if hour_user+hour>23: # if else to solve the +24hours problem
    #    hour_new = hour+hour_user-24
    #    day = day+1
    #    countdown_to = datetime(year,month,day,hour_new,minutes)
    #else:
    #    countdown_to = datetime(year,month,day,hour+hour_user,minutes)

    countdown_to = datetime(year,month,day,hour,minute+2) # testing countdown (time+2minute)
    print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, " Press 'e' to exit at any time.\n")

    while True:

        print_status=True
        while datetime.now() < countdown_to:
            time.sleep(0.05)
            countdown = int((countdown_to - datetime.now()).total_seconds())
        
            if (countdown%10 == 0 and B!=countdown and countdown>0): #countdown every 10 seconds, useful for quick testing, no need to wait one minute
            #if datetime.now().minute != last_minute: #countdown every minute
                time_left_seconds = int((countdown_to - datetime.now()).total_seconds())
                time_converted = str(timedelta(seconds=time_left_seconds))
                print('Time left:', time_converted)
                #print('Time left:', int((countdown_to - datetime.now()).total_seconds() // 60), 'min') # if the countdown is in minute
                print('Time now:', datetime.now(), '\n')
                B=countdown           
                #last_minute = datetime.now().minute # if countdown in minutes 
        
        
            if keyboard.is_pressed("e"):
                alive_status=2
                break
            if (pir2.motion_detected==True or pir1.motion_detected==True):
                prGreen("\nMotion detected, everybody alive!")
                alive_status=1
                time.sleep(1)
                break
                


        if alive_status==1:
            if print_status:
                smiley() # show smiley on sensehat
                print("Automatically adding 24 hours to monitoring.")
                new_day=(datetime.now().day)+1
                countdown_to = datetime(year,month,new_day,hour,minute)
                print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                time.sleep(1)
                sense.show_letter("3",blue)
                print_status=False
            continue

        if keyboard.is_pressed("e"):
            alive_status=2
            break
        if alive_status==0:
            break




    if alive_status == 2:
        print("\n")          
    if alive_status==0:  
        prRed("ALERT, time reached without motion. SEND HELP") 
        dead() # show sad face on sensehat
    time.sleep(2)    
