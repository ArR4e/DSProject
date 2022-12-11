f=open("kinganumbrid.txt")

while True:
    try:
        sisu=f.readline()
        if sisu == "":
            break
        pikkus=2/3 * (float(sisu) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")
        
f.close()
