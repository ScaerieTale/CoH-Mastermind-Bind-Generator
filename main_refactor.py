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
dark_mode = True

# GUI framework
from statistics import median
from tkinter import *

# main window setup
root = Tk()
root.maxsize(1600,900)
root.title("ScaerieTale's Mastermind Bind Generator")

# Content setup

def labels(label_text, size):
    if size == SMALL_TEXT:
        if dark_mode is True:
            Label(text=label_text, font=(FONT_FAMILY, SMALL_TEXT, ), bg=BG_DARK_MODE, fg=FG_DARK_MODE)
        elif dark_mode is not True:
            Label(text=label_text, font=(FONT_FAMILY, SMALL_TEXT, ), bg=BG_LIGHT_MODE, fg=FG_LIGHT_MODE)
    
    if size == MEDIUM_TEXT:
        if dark_mode is True:
            Label(text=label_text, font=(FONT_FAMILY, MEDIUM_TEXT), bg=BG_DARK_MODE, fg=FG_DARK_MODE)
        elif dark_mode is not True:
            Label(text=label_text, font=(FONT_FAMILY, MEDIUM_TEXT), bg=BG_LIGHT_MODE, fg=FG_LIGHT_MODE)

