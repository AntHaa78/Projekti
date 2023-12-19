import time
from datetime import datetime
from datetime import timedelta
import random
import string
import keyboard # only to simulate sensor, can delete later


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

# Color codes for showing colors on sense hat
blue = (0,0,255)
green = (0, 255, 0)
red = (255, 0, 0) 
yellow = (255,255,0)
black = (0,0,0)

# To display a yellow smiley on the sense hat
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



def password_generator(): # basic password generator function, only lower case letters, can adjust lentgh. Used for mode one
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
                                
                                #print(f"\nYou exited the room! If you're not back within {max_time_out_of_room} seconds, your reservation will freed up.")
                                prRed(f"\nYou exited the room! If you're not back within {max_time_out_of_room} seconds, your reservation will freed up.")                           
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
                                    prRed("\nYou took too long to come back! Your reservation is now cancelled.\nPress e to go back to menu")
                                    break

                            elif print_status:
                                print(f"\n{name} is in the room... (press 'y' to exit room (simulate Motion sensor2))")
                                print_status=False
                    else:
                        print("Name and/or password inccorect. Try again") 

            elif print_status:
                
                print(f"\nWaiting for {name} to show up...")
                print("To simulate motion sensor: press 'x' to detect Motion 1(outside) and 'y' to detect motion 2 (inside)")
                print_status=False  

        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nMode ROOM booking exited successfully")
            break

        elif print_status: # if hour is not yet reached start time
            print(f"\nNo reservation at {hour}. Next reservation at {start_time}")   
            print_status=False       


def mode_two():
    print_status = True # Boolean variable to be able to print only once when in while loops
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
        if keyboard.is_pressed("y") or keyboard.is_pressed("x"): # simulate sensors
            prRed("INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER INTRUDER")
            while True: # loop to turn off alarm
                answer=input("Please enter password to desactivate alarm: ")
                if answer == password:
                    print("Alarm desactivated, back to alarm mode")
                    prRed("ALARM MODE ON")
                    break
                if answer == 'e':
                    break
                else:
                    print("Wrong password, alarm still beeping")          
        if keyboard.is_pressed("e"): #exit mode alarm
            print("\nMode ALARM exited successfully")
            break
        elif print_status:
            print("ALARM MODE ON (press x or y to simulate motion sensors)")
            print_status=False


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


    while datetime.now() < countdown_to:
        
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

        if keyboard.is_pressed("y") or keyboard.is_pressed("x"):
            print("\nMotion detected, everybody alive!")
            alive_status=1
            answer = input("\nDo you want to automatically add 12 hours to the countdown? (y/n)")
            if answer=="y":
                hour_plus_twelve=datetime.now().hour+12
                if hour_plus_twelve>23:
                    hour_new = hour_plus_twelve-24
                    day = datetime.now().day+1
                    countdown_to = datetime(year,month,day,hour_new,minute)
                else:
                    countdown_to = datetime(year,month,day,hour_plus_twelve,minute)
                print("\nCountdown initiated at ", datetime.now(), "until", countdown_to, "\n")
                continue
            elif answer=="n":
                print("\nExiting MONITORING MODE")
                break

        if keyboard.is_pressed("e"):
            print("Mode exited, back to menu") 
            alive_status=2
            break

        elif print_status:
           print("(Press x or y to simulate sensors), e to exit")
           print_status=False

   # if alive_status == 1:
       # print("Motion detected, everybody alive! Monitoring OFF") 
   # if alive_status == 2:
        #print("Mode exited, back to menu")          
    if alive_status==0:  
        prRed("ALERT, time reached without motion. SEND HELP") 
    time.sleep(2)    

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
