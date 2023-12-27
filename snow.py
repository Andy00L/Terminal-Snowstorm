# We will need os to clear the screen, radom to generate the snow and time for the delay.
import os
import time
import random

# Snow density
snow_density = 7
delay = 0.2

# Snowflake icons
snowflake = ["❄️", "❅", "❃", "❋", "❉"]

# Get screen size
term = os.get_terminal_size()

# Screen width and height
width = term.columns
height = term.lines

# Create a grid with the height and width of the screen
grid = []
for _ in range(height):
    grid.append([' '] * width)

# Function to draw the grid
def draw_grid():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Hide the cursor
    print('\033[?25l')

    # Output for each row of the grid
    output = ''
    for row in grid:
        output += ''.join(row) + '\n'
    output = output.strip('\n')
    print(output, end='')

# Draw the initial grid
draw_grid()

# Infinite loop to generate snowflakes
while True:
    # Create a new row of snowflakes
    row = []
    for _ in range(width):
        if random.random() < snow_density / 100:
            row.append(random.choice(snowflake))
        else:
            row.append(' ')

    # Add the new row to the grid and remove the last row
    grid.insert(0, row)
    grid.pop()

    # Draw the updated grid
    draw_grid()

    # Wait for a bit before generating the next snowflakes
    time.sleep(delay)
