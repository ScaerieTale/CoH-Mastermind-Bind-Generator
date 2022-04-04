def fileGen1(tier, world_name):
    f = open(f"{tier}.txt", 'w')
f.write(f"""numpad4 petcom_pow {world_name} aggressive
numpad5 petcom_pow zom defensive
numpad6 petcom_pow {world_name} passive
numpad7 petcom_pow {world_name} attack
numpad8 petcom_pow {world_name} follow
numpad9 petcom_pow {world_name} goto
lctrl+decimal petcom_pow {world_name} dismiss""")
f.close()
