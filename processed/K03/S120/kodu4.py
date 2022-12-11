with open("kinganumbrid.txt") as f:
    for line in f.readlines():
        try:
            print(round(2/3 * (float(line) - 2)))
        except:
            print('Vigane sisend')
