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

mid = (end + begin) // 2
 
# b1, e1 = begin, int(0.1 * end)
# b2, e2 = e1, int(0.2 * end)
# b3, e3 = e2, int(0.3 * end)
# b4, e4 = e3, int(0.4 * end)
# b5, e5 = e4 , int(0.5 * end)
# b6, e6 = e5, int(0.6 * end)
# b7, e7 = e6, int(0.7 * end)
# b8, e8 = e7, int(0.8 * end)
# b9, e9 = e8, int(0.9 * end)
# b10, e10 = e9, end

# key_text = ""
# counter = 0
id = str(int(time.time()))

while True:
    ns = [random.randint(begin, mid), random.randint(mid, end)]

    for n in ns:
        hex_key = hs.num_to_hex64(n)
        assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

        if assumed_addr == compressed_addr:
            with open("./privkeys/random-" + "99" + id + ".txt", "w+") as f: f.write(str(n) + ": " + assumed_addr + ": "  + hex_key)
            with open("./success-random-" + "99" + id, "w+"): f.write(__name__ +  " Found Dis")
            print("Found bich")
            exit()

        # counter += 1
        # key_text += str(n) + "\n"

        # if counter % 10000 == 0:
            # with open("random-keys/random101-" + id + ".txt", "a+") as f:
                # f.write(key_text)
                # key_text = ""
