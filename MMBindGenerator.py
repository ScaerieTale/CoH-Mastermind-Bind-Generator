while True:
    masterFile = input("Enter the nickname for your Primary (eg Ninjas, Necro, etc): ")
    tier1 = input("Enter the name or nickname for your Tier 1 pet (eg Genin, Zombie) ")
    tier2 = input("Next, the name of your tier 2 pet: ")
    tier3 = input("And finally your tier 3: ")
    print(f"""Okay, we're almost done!  Next we'll set up your Summon powers to bind them to: 
        Numpad / ({tier1}, Numpad * ({tier2}), Numpad - ({tier3}) and your Upgrade powers.  Ready?""")
        t1Sum = input("I need the EXACT name of your tier 1 summoning power (e.g. Call Thugs, Summon Demonling): ")
        t2Sum = input("Next, your tier 2 (e.g. Call Enforcers): ")
        t3Sum = input("Finally, your t3 (e.g. Call Bruiser): ")
        print(f"So that's {t1sum}, {t2sum} and {t3sum}, got it!")
        print(" Computing...  Okay, last two and your Master file will be complete!")
        buff1 = input("What is the name of your FIRST primary upgrade power (e.g. Equip Thugs): ")
        buff2 = input("Now, what is your SECOND upgrade power? (e.g. Upgrade Equipment): ")
        # create a function to generate and write to a Master file and children
        f = open(f"{masterFile}MM.txt", 'w') # w = mode, i.e. 'Write'
        f.write(f"""numpad0 bindloadfilesilent "\all.txt"
numpad1 bindloadfilesilent "\{tier1}.txt"
numpad2 bindloadfilesilent "\{tier2}"
numpad3 bindloadfilesilent "\{tier3}.txt"
divide powexec_name "summon wolves"
multiply powexec_name "summon lions"
subtract powexec_name "summon dire wolf"
add powexec_name train beasts
numpadenter powexec_name Tame Beasts""")