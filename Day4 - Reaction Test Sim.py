import machine
import time

# Define GPIO pins for the LED and button
led_pin = machine.Pin(14, machine.Pin.OUT)
button_pin = machine.Pin(15, machine.Pin.IN) #delete PULL.UP

# Function to measure reaction time
def reaction_time_tester():
    time.sleep(5)
    led_pin.on()
    start_time = time.ticks_ms() #from the time library, .ticks_ms() measures the measures the time in miliseconds and will assign it to the start_time variable
    
    while True: #this while loop is waiting for the button press
        if button_pin.value() == 1: #if the button pin is press or on which is 1
            end_time = time.ticks_ms()
            reaction_time = end_time - start_time #this is the final reaction time
            print('Reaction Time', reaction_time, 'ms') #this will print a string concat 'Reaction time <variable value> ms'
            break #breaks out of the loop at the end of the if statement
          
    led_pin.off() #once the above runs, turn the LED off
    
reaction_time_tester() #call the function