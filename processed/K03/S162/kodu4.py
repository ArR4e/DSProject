f=open("kinganumbrid.txt")
a=f.readline().strip()
while a!="":
    try:
        pikkus=float(a)
        print(round(2/3*(pikkus-2)))
    except:
        print("vigane sisend")
    a=f.readline().strip()
f.close()
