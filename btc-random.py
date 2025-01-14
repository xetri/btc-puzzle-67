import helpers as hs
import random
import config

while True:
    num = random.randint(config.begin, config.end)
    hex_key = hs.num_to_hex64(num)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./privkeys/random-" + str(num) + ".txt", "w+") as f: f.write(str(num) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success-random-" + str(num), "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()
