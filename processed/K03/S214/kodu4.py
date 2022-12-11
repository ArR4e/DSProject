f = open("kinganumbrid.txt")
i = len(f.readlines())
f.close
f = open("kinganumbrid.txt")
while i>0:
    try:
        kinganumber = f.readline().strip()
        pikkus = 2/3 * (float(kinganumber) - 2)
        print(int(round(pikkus,0)))
    except:
        print("Vigane sisend")
    i-=1