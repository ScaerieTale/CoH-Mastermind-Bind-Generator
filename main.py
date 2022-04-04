from asyncore import write


masterFile = input("Enter the nickname for your Primary (eg Ninjas, Necro, etc): ")
tier1 = input("Enter the name or nickname for your Tier 1 pet (eg Genin, Zombie) ")
tier2 = input("Next, the name of your tier 2 pet: ")
tier3 = input("And finally your tier 3: ")
t1Sum = input("I need the EXACT name of your tier 1 summoning power (e.g. Call Thugs, Summon Demonling): ")
t2Sum = input("Next, your tier 2 (e.g. Call Enforcers): ")
t3Sum = input("Finally, your t3 (e.g. Call Bruiser): ")
print(f"So that's {t1Sum}, {t2Sum} and {t3Sum}, got it!")
buff1 = input("What is the name of your FIRST primary upgrade power (e.g. Equip Thugs): ")
buff2 = input("Now, what is your SECOND upgrade power? (e.g. Upgrade Equipment): ")

# create a function to generate and write to a Master file and children
f = open(f"{masterFile}MM.txt", 'w') # w = mode, i.e. 'Write'
f.write(f"""numpad0 bindloadfilesilent "\all.txt"
numpad1 bindloadfilesilent "\{tier1}.txt"
numpad2 bindloadfilesilent "\{tier2}"
numpad3 bindloadfilesilent "\{tier3}.txt"
divide powexec_name "{t1Sum}"
multiply powexec_name "{t2Sum}"
subtract powexec_name "summon {t3Sum}"
add powexec_name {buff1}
numpadenter powexec_name {buff2}""")
f.close

print("We're in the home stretch.  Now we need to create your 'child' files, the files")
print("that tell your dumdums what to do.")
trueName1 = input("Please enter your Tier 1 minion's name as it appears in the world (e.g. Zombie, Battle Drone, etc): ")
trueName2 = input("Now enter your Tier 2 pet's name as above (e.g. Grave Knight): ")
bobFromAccounting = input("Now enter your tier 3 pet's name as before.")
