fail = open ("kinganumbrid.txt")
rida = fail.readline()
try:
    kinganumber = float(rida)
    pikkus = 2*(kinganumber-2)/3
    for rida in fail:
    print(round(pikkus))
expect:
    print("Vigane sisend")


