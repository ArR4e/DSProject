with open("kinganumbrid.txt", 'rt') as f:
    numbrid = f.readlines()
    for i in numbrid:
        try:
            i = float(i)
            print(round(2 / 3 * (i - 2)))
        except:
            print("Vigane sisend")
