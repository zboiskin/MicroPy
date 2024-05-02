import machine
import time

# Define LED Pin
LED_PIN = 17
led = machine.Pin(LED_PIN, machine.Pin.OUT) #OUT means output

# Define ADC Pin for LDR
#ADC is the analog to digital converter
#Note the ADC pin variable is consistent with the machine.ADC 
# This will be our input pin
ADC_PIN = 26
adc = machine.ADC(machine.Pin(ADC_PIN))

# Define a threshold for the LDR reading below which the LED should turn ON
LIGHT_THRESHOLD = 63000  # This might need adjustment based on your LDR and environment

#Creating the function for the night light
def night_light():
    while True: #forever loop
        light_value = adc.read_u16() #u16 means unsigned, 6 bit number just as a limit setter for values read
        print(light_value) #this just shows us the light value being read
    
        if light_value < LIGHT_THRESHOLD: #if the light amount being read from the photoresistor is less than the read threshold aka dark enough, turn the LED ON or 1
            led.value(1)
        else: #if not, keep the LED off or 0
            led.value(0)
    
        time.sleep(0.5) #check the light level every half second to see if it changed
    
night_light() #calls the function