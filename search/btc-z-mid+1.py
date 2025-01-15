import helpers as hs
import config

i = (config.begin + config.Z) // 2
try:
    with open("./priv/progress-z-mid+1.txt") as f: i = int(f.read())
except: pass

counter = 1
while i < config.Z + 1:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./success-begin-" + str(i) + ".txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        print("Found bich")
        exit()

    i += 1
    if counter % 5000 == 0: 
        with open("./priv/progress-z-mid+1.txt", "w+") as f: f.write(str(i))
    counter += 1
