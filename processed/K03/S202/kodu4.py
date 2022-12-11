r = open("kinganumbrid.txt")

while True:
    kn = r.readline()
    if len(kn) > 0:
        try:
            b = 2/3 * (float(kn) - 2)
            print(round(b))
        except:
            print("Vigane sisend")
    else:
        break

r.close()