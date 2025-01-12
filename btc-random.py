#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs
import random

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 100000000000000000
end   = 0x1fffffffffffffffff

while True:
    num = random.randint(begin, end)
    hex_key = hs.num_to_hex64(num)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == compressed_addr:
        with open("./privkeys/random-" + str(num) + ".txt", "w+") as f: f.write(str(num) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success-random-" + str(num), "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()
