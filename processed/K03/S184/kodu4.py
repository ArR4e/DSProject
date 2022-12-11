f=open("kinganumbrid.txt")
while True:
    king=f.readline()
    if king=="":
       break
    else:
        try:
            kinganr=float(king)
            p = 2/3 * (kinganr - 2)
            pikkus=round(p)
            print(pikkus)
        except:
            print("Vigane sisend")
f.close