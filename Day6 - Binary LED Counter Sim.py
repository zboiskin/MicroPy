import machine
import time

# Define GPIO pins for the 4 LEDs
# Putting the pins in an array makes them easier to call as an index later on
led_pins = [
    machine.Pin(0, machine.Pin.OUT),
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(3, machine.Pin.OUT)
]
button_pin = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)

#Initialize LED stes for 4 LEDs, meaning we are setting all the LED pins to off or 0 to start
led_states = [0] * len(led_pins)

# Function to increment binary counter
# This function loops through all the LEDs and if it is set to 1 then turn it on and if it is 0 then turn it off
def update_led_states():
    for i, led in enumerate(led_pins):
        if led_states[i] == 1:
            led.on()
        else:
            led_off()
            
#Function to increment the binary counter     
#Meaning everytime we press the button we want to increment the count by 1   
#When you hit the button each time the count will go up 1, 2, 3, 4 etc. and not just 1, 1, 1, 1,
def increment_counter():
    #convert LED states to integer
    binary_value = int(''.join(map(str, led_states)), 2) #this first gets the initial binary number currently on the LEDs
    binary_value += 1 #then increases the current value of the LEDs by 1
    #Safeguard to set the number back to 0 if we go over our 15 count limit since we are only using 4 LEDs
    if binary_value >= 16:
        binary_value = 0
    #converts decimal to binary string    
    binary_string = bin(binary_value)[2:]
    #fill in with 0s so it is clean to look at
    binary_string = binary_string.zfill(len(led_pins))
    
    #Update LED states
    #Using the above code that is calculating the binary string, the below will set that LED light to represent the calculated binary string
    for i, bit in enumerate(binary_string):
        led_states[i] = int(bit)
        
# Main loops
while True:
    if button_pin.value() == 0:
        increment_counter()
        update_led_states()
        time.sleep(0.2) #button debounce delay

