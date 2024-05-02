#Import libraries
import machine #library used to talk to our Pico and read/write, set pins
import utime #library that makes our timing functionality work such as timers, pauses, delays between actions etc.

#Defining the LED pins
#Define pins for LEDs
red_pin = machine.Pin(16,machine.Pin.OUT)
yellow_pin = machine.Pin(17,machine.Pin.OUT)
green_pin = machine.Pin(18,machine.Pin.OUT)

#Defining function to turn off all LEDs - kind of like set up in Arduino
def all_off():
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(0)
    
#Main loop to cycle through the values above and time them when to turn on and off
#.value makes the LED an individual value in the above function
#value 0 or 1 makes the LED turn on or off
while True:
    all_off()  # Turn all LEDs off
    
    red_led.value(1)  # Turn red LED on
    utime.sleep(5)  # Wait for 5 seconds
    
    all_off()  # Turn all LEDs off
    
    yellow_led.value(1)  # Turn yellow LED on
    utime.sleep(1)  # Wait for 1 second
    
    all_off()  # Turn all LEDs off
    
    green_led.value(1)  # Turn green LED on
    utime.sleep(4)  # Wait for 4 seconds