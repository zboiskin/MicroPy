#Import libraries
import machine #library used to talk to our Pico and read/write, set pins
import time #library that makes our timing functionality work such as timers, pauses, delays between actions etc.

#Define pins for LEDs
red_pin = machine.Pin(17,machine.Pin.OUT)
yellow_pin = machine.Pin(19,machine.Pin.OUT)
green_pin = machine.Pin(20,machine.Pin.OUT)

#Function to turn on our LEDs in a specific pattern
def traffic_light(): #empty () means it does not require and input parameter
    red_pin.on() #similar to digitalWrite = HIGH
    time.sleep(2) #time for the time library, .sleep to use the sleep function, 2 is for wait 2 seconds
    red_pin.off()
    green_pin.on()
    time.sleep(2) #pause for 2 seconds
    green_pin.off()
    yellow_pin.on()
    time.sleep(1) #pause for 1 second 
    yellow_pin.off()

#Calling our traffic light function
traffic_light()
