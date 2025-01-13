#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs
import random
import time

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 0x100000000000000000
end   = 0x1fffffffffffffffff

# key_text = ""
# counter = 0
id = str(int(time.time()))

while True:
    ns = [random.randint(begin, end) for _ in range(69)] + [random.randint(begin + i, end - i) for i in range(69)]

    for n in ns:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

        if assumed_addr == compressed_addr:
            with open("./privkeys/random-" + "rand69"+ id + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("./success-random-" + "rand69" + id, "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()


