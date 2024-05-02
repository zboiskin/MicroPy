import machine
import time

# Define the GPIO pin for the button
# REMEMBER that this button is equal to physically the 20th pin - GP15 aka button_pin 15 = physical pin 20
button_pin = 15
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Morse code mapping
# This is defined as a SET because it is using {} meaning that it cannot be manipulated and each value is unique
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

#Defining the variables of duration in seconds for dots, dashes and end of letter
dot_duration = 0.2
dash_duration = 0.6
end_of_letter_duration = 1.5 #meaning when you are done 'typing'

#Defining the function to interpret the button presses as dots or dashes 
def interpret_button_press():
    morse_string = '' #once we begin, let's start the string being empty
    while True: #while True means a 'forever' loop
        while button.value() == 1: #while the button value is pressed (or ==1)
            time.sleep(0.05)
        
        # Measure the duration of the button press
        start_time = time.time() #.time is pretty much a timer method - it will measure the time is takes for the action to reach the hardware
        #when the button value is 0 or not pressed, pass out of this loop
        while button.value() == 0:
            pass 
        # end time calculates how long it took to recognize the button is not pressed
        end_time = time.time()
        duration = end_time - start_time
# Overall this measures the time a button is pressed or 1 and stored as start time in the first while loop 
# And how long it takes to get to the button not being pressed or 0 in the second loop
# duration is second it got to NOT being pressed - time the button was being pressed 
        if duration <= dot_duration: #if the press is less than 0.2 seconds defined above
            morse_string += '.' #then the morse letter will be a dot . 
        else: 
            morse_string += '-'  #anything else will be considered a dash 
        
        # Wait to see if the user finishes by seeing if they press the button for longer than 1 second
        #If they have pressed it for more than 1 second, indicating they are finished, then show is the morse code the was done
        start_time = time.time()
        while button.value() == 1:
            if (time.time() - start_time) > end_of_letter_duration:
                return morse_string
                
#function saying to print our morse inputs from the button in our terminal
#if we do press something that is not recognized as a morse letter, print Unrecognized Morse Code
def main():
    print("Input Morse code using the button. A short press is '.', a long press is '-'.")
    print("Wait for more than 1.5 seconds to finish inputting a letter.")
    
    while True:
        morse_string = interpret_button_press()
        for key, value in morse_code.items():
            if value == morse_string:
                print(key)
                break
        else:
            print(f"Unrecognized Morse code: {morse_string}")

if __name__ == "__main__":
    main()