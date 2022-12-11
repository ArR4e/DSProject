with open("kinganumbrid.txt") as f:
    text = f.readlines()
    for line in text:
        try:
            kinganumber = float(line)
            print(round(2/3 * (kinganumber-2)))
        except:
            print("Vigane sisend")