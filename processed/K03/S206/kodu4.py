with open('kinganumbrid.txt') as k:
    while True:
        num = k.readline()
        if num == "":
            break
        try:
            a = float(num)
            pikkus = round(2/3 * (a-2))
            print(pikkus)
        except:
            print("Vigane sisend")
            