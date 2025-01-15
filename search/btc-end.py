import helpers as hs
import config

i = config.end
try:
    with open("./priv/progress-end.txt") as f: i = int(f.read())
except: i = config.begin

counter = 1
while i > config.Z - 1:
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./success-end-" + str(i) + ".txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        print("Found bich")
        exit()

    i -= 1
    if counter % 5000 == 0: 
        with open("./priv/progress-end.txt", "w+") as f: f.write(str(i))
    counter += 1
