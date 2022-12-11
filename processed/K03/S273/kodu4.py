f = open("kinganumbrid.txt")
kinganumber = f.readline()

while kinganumber != "":
    try:
        while kinganumber != "":
            print((2 / 3) * (kinganumber - 2))
    except:
        print("Vigane sisend")
