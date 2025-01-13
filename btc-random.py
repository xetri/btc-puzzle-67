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
    num = random.randint(begin, end)
    hex_key = hs.num_to_hex64(num)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == compressed_addr:
        with open("./privkeys/random-" + str(num) + ".txt", "w+") as f: f.write(str(num) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success-random-" + str(num), "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()

    # counter += 1
    # key_text += str(num) + "\n"

    # if counter % 10000 == 0:
    #     with open("random-keys/btc-random" + id + ".txt", "a+") as f: f.write(key_text)
    #     key_text = ""
