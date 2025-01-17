import helpers as hs
import config
import threading

def Scan(begin, end):
    threading.Thread(target=divide_and_conquer, args=(begin, end)).start()

def divide_and_conquer(begin, end):
    if end - begin <= 1:
        search(begin)
        return

    m = (begin + end) // 2
    threads = [
        threading.Thread(target=ptrDecScan, args=(m, begin)),
        threading.Thread(target=ptrIncScan, args=(m + 1, end)),
        threading.Thread(target=divide_and_conquer, args=(begin, m)),
        threading.Thread(target=divide_and_conquer, args=(m + 1, end)),
    ]
    for t in threads: t.start()

def ptrDecScan(n, delim):
    for i in range(n, delim, -1): search(i)

def ptrIncScan(n, delim):
    for i in range(n, delim + 1): search(i)

def search(i):
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./success-begin-" + str(i) + ".txt", "a+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key + "\n")
        print("Found bich")
        exit()
