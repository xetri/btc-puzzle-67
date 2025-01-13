#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 100000000000000000
begin = begin + int(0.05 * begin)
end   = 0x1fffffffffffffffff
endset = begin + int(0.05 * begin)

i = 105000000029414000

__f = open("./privkeys/progress2.txt")
i = int(__f.read())
__f.close()

counter = 1
while i < endset:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == compressed_addr:
        with open("./privkeys/2.txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success2", "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()

    i += 1

    if counter % 500 == 0: 
        with open("./privkeys/progress2.txt", "w+") as f: f.write(str(i))
    counter += 1
