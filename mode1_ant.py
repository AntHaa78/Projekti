from gpiozero import LED, Button
import time
from signal import pause

# Pin and button numbers 
led = LED(17)
button = Button(2)

""" button.when_pressed = led.on
button.when_released = led.off """

def presstime():
    time_seconds = time.time()
    return time_seconds

def showtime_pressed():
    time_seconds = time.time()
    t = time.ctime(time_seconds)
    print("Key pressed at", t)

def showtime_released():
    time_seconds = time.time()
    t = time.ctime(time_seconds)
    print("Key released at", t)

def combinfunction1():
    global a
    a = presstime()
    showtime_pressed()

def combinfunction2():
    b = presstime()
    showtime_released()
    total_time = b - a
    print("\nThe key was pressed for" + total_time + "seconds")



button.when_pressed = combinfunction1
button.when_released = combinfunction2

pause()