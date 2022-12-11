f = open("kinganumbrid.txt")

while True:
    sisu = f.readline()
    if sisu == "":
            break
    try:
        number = float(sisu)
        pikkus = round(2/3 * (number - 2))
        print(pikkus)
    except:
        print("Vigane sisend")
        
f.close()
