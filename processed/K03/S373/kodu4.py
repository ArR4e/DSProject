f = open("kinganumbrid.txt")
i = 0
for i in f:
    try:
        float(i)
        i = 2/3*((float(i) - 2))
        print(round(i))
    except ValueError:
        print("Vigane sisend")
f.close()
    