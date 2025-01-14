import helpers as hs
import random
import config

mid = (config.end + config.begin) // 2 + 1
 
while True:
    ns = [random.randint(config.begin, mid), random.randint(mid, config.end)]

    for n in ns:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

        if assumed_addr == config.comp_addr:
            with open("./privkeys/random-" + "99-" + str(n) + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("./success-random-" + "99-" + str(n), "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()
