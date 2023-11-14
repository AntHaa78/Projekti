from gpiozero import LED, Button
import time
from signal import pause

# Pin and button numbers 
led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
