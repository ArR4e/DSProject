f=open("kinganumbrid.txt")
f1=f.readline()
while f1 != "":
    try:
        pikkus=round(2/3*(float(f1)-2))
        print(pikkus)
    except ValueError:
        print("vigane sisend")
    
    f1=f.readline()
f.close()
