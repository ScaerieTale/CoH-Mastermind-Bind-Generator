# 20 questions!  Will replace this with a graphical interface ASAP
master_file = input("Enter the nickname for your Primary (eg Ninjas, Necro, etc): ")
tier_1 = input("Enter the name or nickname for your Tier 1 pet (eg Genin, Zombie) ")
tier_2 = input("Next, the name of your tier 2 pet: ")
tier_3 = input("And finally your tier 3: ")
tier_1_summon = input("I need the EXACT name of your tier 1 summoning power (e.g. Call Thugs, Summon Demonling): ")
tier_2_summon = input("Next, your tier 2 (e.g. Call Enforcers): ")
tier_3_summon = input("Finally, your tier 3 (e.g. Call Bruiser): ")
buff_1 = input("What is the name of your FIRST primary upgrade power (e.g. Equip Thugs): ")
buff_2 = input("Now, what is your SECOND upgrade power? (e.g. Upgrade Equipment): ")

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
numpadenter powexec_name {buff_2}
''')
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