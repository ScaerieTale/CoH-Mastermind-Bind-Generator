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
while True:
    title2 = input("Enter your LT (second pet's eg Enforcer, GraveKnight, ProtBot) common name ")
    ltName = input("Enter your LT pet's Power name (e.g. Call Jounin)")
    f = open(f"{title2}.txt", 'w')
    f.write(f"""numpad4 petcom_pow {ltName} aggressive
numpad5 petcom_pow {ltName} defensive
numpad6 petcom_pow {ltName} passive
numpad7 petcom_pow {ltName} attack
numpad8 petcom_pow {ltName} follow
numpad9 petcom_pow {ltName} goto
lctrl+decimal petcom_pow {ltName} dismiss""")
    f.close