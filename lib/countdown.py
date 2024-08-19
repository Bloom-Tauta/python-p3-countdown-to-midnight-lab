# your code goes here!
import time

def countdown(number):
    i = number
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
        # if i == 0:
        
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    countdown(number)
    time.sleep(number)

# countdown_with_sleep(10)