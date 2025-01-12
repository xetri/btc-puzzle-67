import helpers as hs
import time

hexs, compaddrs = [], []

with open("./pvkey.txt", "r") as p:
    txt = p.read()
    pv_addrs = txt.split("\n")
    for pv in pv_addrs: 
        if pv != '':
            (hex, compaddr) = pv.split(" ")
            hexs.append(hex)
            compaddrs.append(compaddr)

prevtime = time.time()
i = 0
while i < len(hexs):
    privkey, addr = hexs[i], compaddrs[i]

    gotaddr = hs.pvkhex_to_address_compressed(privkey)

    print("True(^)" if gotaddr == addr else "False (X)")

    i += 1
endtime = time.time()

print("Took: ", (endtime - prevtime) * 1000 , " ms")
