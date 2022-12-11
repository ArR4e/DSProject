f = open("kinganumbrid.txt")

for rida in f:
    try:
        nr = float(rida.strip())
        print(round(2/3 * (nr - 2)))
    except:
        print("Vigane sisend")
 