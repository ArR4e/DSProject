#pikkus = 2/3 * (kinganumber - 2)
m = open("kinganumbrid.txt")
for line in m:
    try:
        n = float(line)
        n = round( 2/3 * (n - 2))
        print(n)
    except:
        print("Vigane sisend")





