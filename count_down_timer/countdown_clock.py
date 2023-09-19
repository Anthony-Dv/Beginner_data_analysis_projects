# This is my attempt to recreate countdown timer in python

import time
from playsound import playsound
# get how may seconds to count down
my_time = int(input("Please enter a number of seconds you want to count down.\n"))

# count down from my_time and display remaining seconds.
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}\r", end="")
    time.sleep(1)

print("00:00:00")
print("Timer is up!")
# play iphone timer sound when time is up
playsound("/Users/antonindvoracek/Documents/Programming/Begginer_python_projects/iphone_timer_sound.mp3")