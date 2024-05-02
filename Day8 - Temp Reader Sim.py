from machine import ADC #adc is a module will help us read analog pins and convert it to digital data
import time

adc = machine.ADC(4) #ADC 4 is the 5th ADC pin and the pin we can read from the built in temp reader

while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65536)) #this reads the 3.3 volt pin and divides it by the 65536 bits which is the max value we can get from the pin
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721 #from the calculation above, we can get the celcius
    temp_fahrenheit=32+(1.8*temperature_celcius) #from the celcius above, we can calc the fahrenheit
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit)) #print the calc values from above
    time.sleep_ms(500)