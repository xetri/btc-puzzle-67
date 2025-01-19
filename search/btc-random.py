import threading
import helpers as hs
import random
import config

def search(i):
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./success-begin-" + str(i) + ".txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        print("Found bich")
        exit()

while True:
    nums = [random.randint(config.begin, config.Z + 1), random.randint(config.bR - 1, config.end), random.randint(config.begin, config.end)]

    for n in nums: threading.Thread(target=search, args=(n,)).start()
