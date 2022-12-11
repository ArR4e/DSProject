with open("kinganumbrid.txt", "r") as f:
    for line in f:
        try:
            kinganumber = float(line)
            print(round(2/3 * (kinganumber - 2)))
        except:
            print("Vigane sisend.")



    