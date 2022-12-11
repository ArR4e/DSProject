file = open("kinganumbrid.txt")
filesisu = file.readlines()

for line in filesisu:
    try:
        x = (2/3) * (float(line) - 2)
        print(round(x))
    except:
        print("Vigane sisend")