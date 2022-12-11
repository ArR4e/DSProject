f = open("kinganumbrid.txt", encoding="UTF-8")

sisu = f.readlines()

for i in range(len(sisu)):
    try:
        kinganumber = float(sisu[i].strip())
        pikkus = 2/3 * (kinganumber - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
        
f.close()
