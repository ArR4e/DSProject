f = open("kinganumbrid.txt")
while True:
    try:
        kingaNr = f.readline()
        if kingaNr == "":
            break
        kinganumber = float(kingaNr.strip())
        kinga_pikkus = round(2/3 * (kinganumber - 2))
        print(kinga_pikkus)
    except:
        print("Vigane sisend")

