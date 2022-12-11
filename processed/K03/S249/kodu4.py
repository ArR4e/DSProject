#fail = input("Lähtefaili nimi: ")
fail = open("kinganumbrid.txt", encoding="UTF-8")
for rida in fail:
    try:
        e = float(rida)
        pikkus = round(2/3 * (float(e) - 2))
        print(pikkus)
        
    
    except:
        print("Vigane sisend")
    