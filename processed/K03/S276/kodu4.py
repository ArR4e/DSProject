n=open("kinganumbrid.txt")
for rida in n:
    try:
        kinganr=float(rida.strip())
        a=round(2/3*(kinganr-2))
        print(a)
    except:
        print("Vigane sisend")