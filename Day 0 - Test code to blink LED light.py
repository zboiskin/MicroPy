import machine
import time

led = machine.Pin('LED', machine.Pin.OUT) #configure LED Pin as an output pin

while True:
    led.value(True) #turn on LED 
    time.sleep(1) #pause for 1 second
    led.value(False) #turn off the LED
    time.sleep(1) #pause for one second
                  #continue looping through pretty much forever because True is always True