fail = open("kinganumbrid.txt", encoding="UTF-8")
sisu = fail.read().split("\n")
fail.close()

if sisu == [""]:
    print("")
else :
    for i in sisu :
        try:
            arv = float(i)
            pikkus = round(2/3 * (arv - 2))
            print(pikkus)
        except:
            print("Vigane sisend")
        
        
