file=open("kinganumbrid.txt")
for rida in file:
    try:
        a=float(rida)
        print(round(2/3*(a-2)))
    except ValueError:
        print("Vigane sisend")
file.close()