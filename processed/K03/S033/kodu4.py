f = open("kinganumbrid.txt")

while True:
    kinganr = f.readline().strip()
    if kinganr == "":
        break
    else:
        try:
            pikkus = 2 / 3 * (float(kinganr) - 2)
            print(round(pikkus))
        except:
            print("Vigane sisend.")
            

f.close()