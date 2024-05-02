import machine
import time

# Initialize button on GPIO 15
button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

# Initialize LED on GPIO 14 as a PWM pin
led = machine.PWM(machine.Pin(0))
