# We will need os to clear the screen, radom to generate the snow and time for the delay.
import os
import time
import random

snow_density = 5
delay = 0.3

snowflake = ["❄️","❅","❃","❋","❉"]

term = os.get_terminal_size()

width = term.columns
height = term.lines

print(width, height)
