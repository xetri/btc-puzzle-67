f = open("keys.txt")
data = f.read()
f.close()

ls = []
for l in data.split("\n"):
    if l == '': continue
    
    metas = l.split(" ")
    r = metas[0].split(":")
    ls.append(
            {
                "range": [int(r[0]), int(r[1], 16)],
                "hex"  : int(metas[1], 16),
            }
    )

for l in ls:
    b, e = l["range"]
    h = l["hex"]

    print("Begin: ", b)
    print("End: ", e)
    print("Key: ", h)

    print("End - begin: ", e - b)
    print("End + begin: ", b + e)

    # print("Hash / begin = ", h / b)
    # print("Hash / end = ", h / e)
    # print("begin / hash = ", b / h)
    # print("end / hash = ", e / h)
    # print("begin / end = ", b / e)
    # print("end / begin = ", e / b)
    # print("(end - begin)/hash = ", (e - b)/ h)
    # print("(end + begin)/hash = ", (e + b)/ h)
    # print("(begin * end)/hash = ", round((b * e) / h))
    print("-----------------------")



    
