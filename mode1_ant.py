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
