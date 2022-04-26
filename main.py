# Created with Python 3.10.  If I'm not mistkaen, it
# *should* compile on most versions of Python 3 as
# I'm not using any special features (that I know of...)

# GUI framework
from tkinter import *

# main window setup
root = Tk()
root.maxsize(1600,900)
root.title("ScaerieTale's MM Bind Generator")

# get the information from forms when Run is clicked
buff_1 = ""
buff_2 = ""
def run_clicked():
    master_file = entry_master.get()
    tier_1 = entry_t1.get()
    tier_2 = entry_t2.get()
    tier_3 = entry_t3.get()
    tier_1_summon = entry_t1_summon.get()
    tier_2_summon = entry_t2_summon.get()
    tier_3_summon = entry_t3_summon.get()
    buff_1 = entry_buff_1.get()
    buff_2 = entry_buff_2.get()

    
    # "Master" file generator as a *MM.txt file :)
    file = open(f"{master_file}MM.txt", 'w')
    file.write(f'''numpad0 bindloadfilesilent "\all.txt"
numpad1 bindloadfilesilent "\{tier_1}.txt"
numpad2 bindloadfilesilent "\{tier_2}.txt"
numpad3 bindloadfilesilent "\{tier_3}.txt"
divide powexec_name "{tier_1_summon}"
multiply powexec_name "{tier_2_summon}"
subtract powexec_name "{tier_3_summon}"
add powexec_name {buff_1}
numpadenter powexec_name {buff_2}''')
    file.close()

    # So, I don't fully understand WHY this works, but I'm not
    # going to complain either.  Basically setting up the pets
    # as a dictionary like this, lets me call both pet nickname
    # (for the file name) and pet summon name (fr ingame use) within
    # a single for loop.
    pets = {
        tier_1: tier_1_summon,
        tier_2: tier_2_summon,
        tier_3: tier_3_summon
    }
    # "child" pet files generator
    for pet, summon in pets.items():
        file = open(f"{pet}.txt", 'w')
        file.write(f"""numpad4 petcom_pow {summon} aggressive
numpad5 petcom_pow {summon} defensive
numpad6 petcom_pow {summon} passive
numpad7 petcom_pow {summon} attack
numpad8 petcom_pow {summon} follow
numpad9 petcom_pow {summon} goto
lctrl+decimal petcom_pow {summon} dismiss""")
        file.close()

    file = open("all.txt", 'w')
    file.write("""numpad4 petcom_all aggressive
numpad5 petcom_all defensive
numpad6 petcom_all passive
numpad7 petcom_all attack
numpad8 petcom_all follow
numpad9 petcom_all goto
lctrl+decimal petcom_all dismiss""")
    file.close()

# labels
master_label = Label(justify="right", text="""Name your Main
MM.txt file.  This can be anything you want.""").grid(row=0, column=0)
tier_1_label = Label(justify="right",text="Enter Tier 1 pet nickname:").grid(row=1, column=0)
tier_2_label = Label(justify="right",text="Enter Tier 2 pet nickname:").grid(row=2, column=0)
tier_3_label = Label(justify="right",text="Enter Tier 3 pet nickname:").grid(row=3, column=0)

summon_explanation = Label(justify="right",text="""For the next three fields
please enter your pets' names EXACTLY as they
appear in game:""").grid(row=4, column=0)

tier_1_summon_label = Label(justify="right",text="Summoned tier 1:").grid(row=5, column=0)
tier_2_summon_label = Label(justify="right",text="Summoned tier 2:").grid(row=6, column=0)
tier_3_summon_label = Label(justify="right",text="Summoned tier 3:").grid(row=7, column=0)

buffs_label = Label(justify="right",text="""Enter the two CLASS PRIMARY
buffs below (NOT any secondary buffs)""").grid(row=8, column=0)
buff_1_label = Label(justify="right",text="Buff 1 (level 6):").grid(row=9, column=0)
buff_2_label = Label(justify="right",text="Buff 2 (level 32):").grid(row=10, column=0)


# Functions (fields, button, etc.)
entry_master = Entry(justify="left")
entry_master.grid(row=0, column=1)

entry_t1 = Entry(justify="left",)
entry_t1.grid(row=1, column=1)

entry_t2 = Entry(justify="left",)
entry_t2.grid(row=2, column=1)

entry_t3 = Entry(justify="left",)
entry_t3.grid(row=3, column=1)

spacer_1 = Label(text="          ").grid(row=4, column=1)

entry_t1_summon = Entry(justify="left",)
entry_t1_summon.grid(row=5, column=1)

entry_t2_summon = Entry(justify="left",)
entry_t2_summon.grid(row=6, column=1)

entry_t3_summon = Entry(justify="left",)
entry_t3_summon.grid(row=7, column=1)

spacer_2 = Label(text="          ").grid(row=8, column=1)


entry_buff_1 = Entry(justify="left",)
entry_buff_1.grid(row=9, column=1)

entry_buff_2 = Entry(justify="left",)
entry_buff_2.grid(row=10, column=1)

run_button = Button(justify="left",text="Run", command=run_clicked)
run_button.grid(row=11, column=1)

root.mainloop()
