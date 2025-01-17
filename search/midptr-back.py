import helpers as hs
import config
import threading

def Scan(begin, end):
    t1, t2 = threading.Thread(target=Down, args=(begin, end)), threading.Thread(target=Up, args=(begin, end))

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()

def Down(begin, end):
    m = (begin + end) // 2
    
    tc1, tc2 = threading.Thread(target=ptrDecScan, args=(m, begin)), threading.Thread(target=ptrIncScan, args=(m, end))
    td1, td2 = threading.Thread(target=Down, args=(begin, m)), threading.Thread(target=Down, args=(m, end))
    tu1, tu2 = threading.Thread(target=Up, args=(begin, m)), threading.Thread(target=Up, args=(m, end))

    tc1.start()
    tc2.start()
    td1.start()
    td2.start()
    tu1.start()
    tu2.start()

    # tc1.join()
    # tc2.join()
    # td1.join()
    # td2.join()
    # tu1.join()
    # tu2.join()

def Up(begin, end):
    m = (begin + end) // 2
    
    tc1, tc2 = threading.Thread(target=ptrDecScan, args=(m, begin)), threading.Thread(target=ptrIncScan, args=(m, end))
    td1, td2 = threading.Thread(target=Down, args=(begin, m)), threading.Thread(target=Down, args=(m, end))
    tu1, tu2 = threading.Thread(target=Up, args=(begin, m)), threading.Thread(target=Up, args=(m, end))

    tc1.start()
    tc2.start()
    td1.start()
    td2.start()
    tu1.start()
    tu2.start()

    # tc1.join()
    # tc2.join()
    # td1.join()
    # td2.join()
    # tu1.join()
    # tu2.join()

def ptrDecScan(n, delim):
    i = n
    while i > delim:
        search(i)
        i -= 1

def ptrIncScan(n, delim):
    i = n
    while i < delim:
        search(i)
        i += 1

def search(i):
    hex_key = hs.num_to_hex64(i)
    assumed_addr = hs.pvkhex_to_address_compressed(hex_key)

    if assumed_addr == config.comp_addr:
        with open("./success-begin-" + str(i) + ".txt", "w+") as f: f.write(str(i) + ": " + assumed_addr + ": "  + hex_key)
        print("Found bich")
        exit()
