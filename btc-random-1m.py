#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs
import random
import time

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 100000000000000000
end   = 0x1fffffffffffffffff

b1, e1 = begin, int(0.2 * end)
b2, e2 = e1, int(0.4 * end)
b3, e3 = e2, int(0.6 * end)
b4, e4 = e3, int(0.8 * end)
b5, e5 = e4, end
# b6, e6 = e5, int(0.6 * end)
# b7, e7 = e6, int(0.7 * end)
# b8, e8 = e7, int(0.8 * end)
# b9, e9 = e8, int(0.9 * end)
# b10, e10 = e9, end

id = str(int(time.time()))
# key_text = ""
# counter = 0
while True:
    ns = [random.randint(b1, e1), random.randint(b2, e2), random.randint(b3, e3), random.randint(b4, e4), random.randint(b5, e5)]

    for n in ns:
        # key_text += str(n) + "\n"
        for i in range(1, 1000000):
            # counter += 3
            if n + i < end:
                # key_text += str(n + i) + "\n"
                hex_key = hs.num_to_hex64(n + i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == compressed_addr:
                    with open("./privkeys/random-" + "1m" + ".txt", "w+") as f: f.write(str(n + i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "1m", "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()
            if n - i > begin:
                # key_text += str(n - i) + "\n"
                hex_key = hs.num_to_hex64(n - i)
                assumed_addr = hs.pvkhex_to_address_compressed(hex_key)
                if assumed_addr == compressed_addr:
                    with open("./privkeys/random-" + "1m" + ".txt", "w+") as f: f.write(str(n - i) + ": " + assumed_addr + ": "  + hex_key)
                    with open("./success-random-" + "1m", "w+"): f.write(__name__ +  " Found Dis")
                    print("Found bich")
                    exit()

            # if counter % 9000 == 0:
            #     with open("./random-keys/btc-random-1m" + id + ".txt", "a+") as f:
            #         f.write(key_text)
            #         key_text = ""
