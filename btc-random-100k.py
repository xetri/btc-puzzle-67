import helpers as hs
import random
import config

mid = (config.end + config.begin) // 2

while True:
    ns = [random.randint(config.begin, mid), random.randint(mid, config.end)]

    for n in ns:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
        if assumed_addr == config.comp_addr:
            with open("./privkeys/random-" + "100k-" + str(n) + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("./success-random-" + "100k-" + str(n), "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()
        for i in range(1, 100000):
            if n + i < config.end:
                hex_key = hs.num_to_hex64(n + i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == config.comp_addr:
                    with open("./privkeys/random-" + "100k-" + str(n + i) + ".txt", "w+") as f: f.write(str(n + i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "100k-" + str(n + i), "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()
            if n - i > config.begin:
                hex_key = hs.num_to_hex64(n - i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == config.comp_addr:
                    with open("./privkeys/random-" + "100k-" + str(n - i) + ".txt", "w+") as f: f.write(str(n - i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "100k-" + str(n - i), "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()
