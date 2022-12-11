f = open("C:/Users/elise/OneDrive/Töölaud/kinganumbrid.txt", "r")
line = f.readline()
while line:
    try:
        jalanumber = float(line)
        labapikkus = 2/3 * (jalanumber - 2)
        print(round(labapikkus))
    except:
        print("Vigane sisend")
    line = f.readline()
f.close()
              