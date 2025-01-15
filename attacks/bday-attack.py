import helpers as hs
import random
from config import metas

while True:
    for x in metas:
        n = random.randint(x[0], x[1])
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

        if assumed_addr in x[2]:
            with open("./bday-attack-key-"  + str(n) + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("../success-bday-attack-"  + str(n), "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()
