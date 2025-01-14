import helpers as hs
import config

i = config.begin
try:
    with open("./privkeys/progress1.txt") as f: i = int(f.read())
except: i = config.begin

counter = 1
while i < config.end:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./privkeys/1.txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        with open("./success1", "w+"): f.write(__name__ +  " Found Dis")
        print("Found bich")
        exit()

    i += 1
    if counter % 10000 == 0: 
        with open("./privkeys/progress1.txt", "w+") as f: f.write(str(i))
    counter += 1

