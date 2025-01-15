import helpers as hs
import random
import config

while True:
    nums = [random.randint(config.begin, config.Z + 1), random.randint(config.bR - 1, config.end)]

    for n in nums:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

        if assumed_addr == config.comp_addr:
            with open("./success-random-" + str(n), "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            print("Found bich")
            exit()
