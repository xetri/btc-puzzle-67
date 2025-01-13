#https://privatekeys.pw/puzzles/bitcoin-puzzle-tx#p69
#Range: 100000000000000000:1fffffffffffffffff
#Compressed Address: 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG
# 6.9 BTC

import helpers as hs

compressed_addr = "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG"

begin = 0x100000000000000000
end   = 0x1fffffffffffffffff

end = (end + begin) // 2

# i = end

__f = open("./privkeys/progress-half-1.txt")
i = int(__f.read())
__f.close()

counter = 1
while i > begin:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == compressed_addr:
        with open("./privkeys/half-1.txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success-half-1", "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()

    i -= 1
    if counter % 10000 == 0: 
        with open("./privkeys/progress-half-1.txt", "w+") as f: f.write(str(i))
    counter += 1

