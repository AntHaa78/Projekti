from modes import *

# Main file for working in terminal.
# issues : input staying in terminal, any way to remove directly after entering them? Mostly due to keyboard methods (doesnt press enter). Same issue with sensors?





initAnimation()
while True:
	mode_chosen=input("\nPlease choose a mode: \n1: Room booking\n2: Alert System \n3: Monitoring system \ne: EXIT\n\n")
	if mode_chosen=="1":
		sense.show_letter(mode_chosen,blue)
		mode_one()
		sense.clear()
		back_to_menu()
		continue	
			
	if mode_chosen=="2":
		sense.show_letter(mode_chosen,blue)
		mode_two()
		sense.clear()		
		back_to_menu()
		continue		
		
	if mode_chosen=="3":
		sense.show_letter(mode_chosen,blue)
		mode_three()
		sense.clear()
		back_to_menu()
		continue	
			
	if (mode_chosen=="e" or mode_chosen=="ee"):
		print("Exiting. BYE")
		sense.clear()
		#time.sleep(1)
		exit()
		
	else:
		print("\nCommand not recognised. Please choose 1-4")
