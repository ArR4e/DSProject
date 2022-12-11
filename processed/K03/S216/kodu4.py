fail = open("kinganumbrid.txt", encoding="UTF-8")
for rida in fail:
    try:
        rida = float(rida)
        nr = 2/3 * (rida - 2)
        print(round(nr))
    except:
        print("Vigane sisend")
    
