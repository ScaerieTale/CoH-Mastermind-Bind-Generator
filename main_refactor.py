# Constants
BG_DARK_MODE = "#6c1e00"
FG_DARK_MODE = "#a58ec3"
BG_LIGHT_MODE = "#7fafff"
FG_LIGHT_MODE = "#6e50af"
FONT_FAMILY = "arial, sans"
SMALL_TEXT = 12
MEDIUM_TEXT = 18
LARGE_TEXT = 28

# Defaults
font_size = MEDIUM_TEXT
font_setup = (FONT_FAMILY, font_size)
dark_mode = True

# Set up Dark/Light Mode switch functionality
if dark_mode is True:
    background_color = BG_DARK_MODE
    foreground_color = FG_DARK_MODE
else:
    background_color = BG_LIGHT_MODE
    foreground_color = FG_LIGHT_MODE
 

# GUI framework
from statistics import median
from tkinter import *
from turtle import back

# main window setup
root = Tk()
root.maxsize(1600,900)
root.title("ScaerieTale's Mastermind Bind Generator")

# Functions




# Labels
test_label = Label(text="Testing", font=font_setup, bg=background_color, fg=foreground_color)
test_label.pack()





















root.mainloop()























