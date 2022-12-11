f=open("kinganumbrid.txt")
for rida in f:
    try:
        a=float(rida)
        print(round(2/3*(a-2)))
    except ValueError:
        print("Sisend on vigane")
f.close()