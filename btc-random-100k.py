#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs
import random

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 100000000000000000
end   = 0x1fffffffffffffffff

b1, e1 = begin, int(0.1 * end)
b2, e2 = e1, int(0.2 * end)
b3, e3 = e2, int(0.3 * end)
b4, e4 = e3, int(0.4 * end)
b5, e5 = e4 , int(0.5 * end)
b6, e6 = e5, int(0.6 * end)
b7, e7 = e6, int(0.7 * end)
b8, e8 = e7, int(0.8 * end)
b9, e9 = e8, int(0.9 * end)
b10, e10 = e9, end

while True:
    ns = [random.randint(b1, e1), random.randint(b2, e2), random.randint(b3, e3), random.randint(b4, e4), random.randint(b5, e5), random.randint(b6, e6), random.randint(b7, e7), random.randint(b8, e8), random.randint(b9, e9), random.randint(b10, e10)] 

    for n in ns:
        for i in range(100000):
            if n + i < end:
                hex_key = hs.num_to_hex64(n + i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == compressed_addr:
                    with open("./privkeys/random-" + "100k" + ".txt", "w+") as f: f.write(str(n + i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "100k", "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()
            elif n - i > begin:
                hex_key = hs.num_to_hex64(n - i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == compressed_addr:
                    with open("./privkeys/random-" + "100k" + ".txt", "w+") as f: f.write(str(n - i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "100k", "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()
