kinganumber=0
pikkus=0

f=open("kinganumbrid.txt")
while True:
    try:
        a=f.readline()
        kinganumber=float(a)
        pikkus = 2/3 * (kinganumber - 2)
        print(round(pikkus))
    except:
        if not a:
            break
        print("Vigane sisend")
f.close()