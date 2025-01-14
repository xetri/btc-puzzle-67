import helpers as hs
import random
import config

while True:
    ns = [random.randint(config.begin, config.end) for _ in range(69)] + [random.randint(config.begin + i, config.end - i) for i in range(69)]

    for n in ns:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
        if assumed_addr == config.comp_addr:
            with open("./privkeys/random-" + "rand69-"+ str(n) + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("./success-random-" + "rand69-" + str(n), "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()


