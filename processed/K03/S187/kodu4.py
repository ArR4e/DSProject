f = open("kinganumbrid.txt", "r")

for n in f.readlines():
    try:
        print(round(2/3 * (float(n) - 2)))
    except:
        print("Vigane sisend")