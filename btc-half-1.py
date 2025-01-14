import helpers as hs
import config

i = (config.end + config.begin) // 2 
try:
    with open("./privkeys/progress-half-1.txt") as f: i = int(f.read())
except: i = (config.end + config.begin) // 2

counter = 1
while i > config.begin:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./privkeys/half-1.txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success-half-1", "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()

    i -= 1
    if counter % 10000 == 0: 
        with open("./privkeys/progress-half-1.txt", "w+") as f: f.write(str(i))
    counter += 1

