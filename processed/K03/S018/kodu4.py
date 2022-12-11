with open("kinganumbrid.txt", "r") as f:
    sõne = f.read()
    if len(sõne) > 0:
        list = sõne.split("\n")
        p = len(list)
        i = 0
        while i < p:
            try:
                kinganumber = float(list[i])
                pikkus = round(2/3 * (kinganumber - 2))
                print(pikkus)
                i += 1
            except:
                print("Vigane sisend")
                i += 1