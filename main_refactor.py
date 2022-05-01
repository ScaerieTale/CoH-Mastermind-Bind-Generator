# Constants
BG_VILLAIN_MODE = "#6c1e00"
BG_HERO_MODE = "#6e50af"
FG_COLOR = "#D5BEDF"
FONT_FAMILY = "arial, sans"
SMALL_TEXT = 12
MEDIUM_TEXT = 18
LARGE_TEXT = 28

# Defaults
font_size = MEDIUM_TEXT
font_setup = (FONT_FAMILY, font_size)
villain_mode = True

# Set up Hero/Villain Mode switch functionality
if villain_mode is True:
    background_color = BG_VILLAIN_MODE
else:
    background_color = BG_HERO_MODE
 

# GUI framework
from tkinter import *

# main window
root = Tk()
root.maxsize(1600,900)
root.title("ScaerieTale's Mastermind Bind Generator")
root.config(bg=background_color)
root.minsize(300, 300)


# TODO: Hero/Villain Mode Switch
# This will consist of two separate buttons, one red and one blue.
# When in hero mode (blue BG), a red Villain Mode button will display
# Vice Versa in Villain mode.  The "Run" button will also be themed
# And, I want to add a themed File Browser button/field

# TODO Functions
# So the buttons do things when clicked



# TODO: Labels




# TODO Entry fields
# Including a new File Browser entry



# TODO Buttons (See repo to see what they'll look like)
# Run button, File Browser button (to select where to save the files)
# Hero/Villain Mode button (To change the color scheme)




# TODO Migrate the "guts" of the code so it actually functions










root.mainloop()























