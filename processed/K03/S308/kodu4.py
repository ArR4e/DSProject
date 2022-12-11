f1=open("kinganumbrid.txt")
f2=open("cm", "w")

for rida in f1:
    try:
        nr=2/3*(float(rida)-2)
        nr=round(nr)
        f2.write(str(nr))
        print(nr)
    except:
        print("Vigane sisend")


f1.close()
f2.close()
