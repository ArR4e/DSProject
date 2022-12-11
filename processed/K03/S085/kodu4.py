f = open("kinganumbrid.txt")

for line in f:
    try:
        kinganumber = float(line.strip())
        kinganr = 2/3 * (kinganumber - 2 )
        pikkus = round(kinganr)
        print(pikkus)
    except:
        print("Vigane sisend")          
f.close()
    

