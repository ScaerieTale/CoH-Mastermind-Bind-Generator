# This script will open a command line interface (CLI) and generate a .txt file
# titled the user's choice and then insert the pet summoning power name into
# the appropriate pet command and save the new file within whatever directory the
# script was run from and will continue looping until you type 'q' to quit.

while True:
    title = input("Name your .txt file (i.e. Jounin, Commando, etc - 'q' to quit): ")
    minName = input("What is the pet power name? (eg Call Thugs)  ")
    if title == 'q':
        break
    else: 
    #creates a function to open, edit, and close a pet txt file
        f = open(f"{title}.txt", 'w') # 'w' = mode, i.e. 'write'
        f.write(f"""numpad4 petcom_pow {minName} aggressive
numpad5 petcom_pow {minName} defensive
numpad6 petcom_pow {minName} passive
numpad7 petcom_pow {minName} attack
numpad8 petcom_pow {minName} follow
numpad9 petcom_pow {minName} goto
lctrl+decimal petcom_pow {minName} dismiss""")
        f.close()