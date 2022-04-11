master_file = input("Enter the nickname for your Primary (eg Ninjas, Necro, etc): ")
tier_1 = input("Enter the name or nickname for your Tier 1 pet (eg Genin, Zombie) ")
tier_2 = input("Next, the name of your tier 2 pet: ")
tier_3 = input("And finally your tier 3: ")
tier_1_summon = input("I need the EXACT name of your tier 1 summoning power (e.g. Call Thugs, Summon Demonling): ")
tier_2_summon = input("Next, your tier 2 (e.g. Call Enforcers): ")
tier_3_summon = input("Finally, your tier 3 (e.g. Call Bruiser): ")
buff_1 = input("What is the name of your FIRST primary upgrade power (e.g. Equip Thugs): ")
buff_2 = input("Now, what is your SECOND upgrade power? (e.g. Upgrade Equipment): ")

f = open(f"{master_file}MM.txt", 'w')
f.write(f'''numpad0 bindloadfilesilent "\all.txt"
numpad1 bindloadfilesilent "\{tier_1}.txt"
numpad2 bindloadfilesilent "\{tier_2}.txt"
numpad3 bindloadfilesilent "\{tier_3}.txt"
divide powexec_name "{tier_1_summon}"
multiply powexec_name "{tier_2_summon}"
subtract powexec_name "{tier_3_summon}"
add powexec_name {buff_1}
numpadenter powexec_name {buff_2}
''')
# f = open(f"{title}.txt", 'w')
# f.write(f"""numpad4 petcom_pow {minName} aggressive
# numpad5 petcom_pow {minName} defensive
# numpad6 petcom_pow {minName} passive
# numpad7 petcom_pow {minName} attack
# numpad8 petcom_pow {minName} follow
# numpad9 petcom_pow {minName} goto
# lctrl+decimal petcom_pow {minName} dismiss""")
#         f.close()
#
