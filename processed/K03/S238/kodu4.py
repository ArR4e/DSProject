fail = open("kinganumbrid.txt", "r" , encoding="UTF-8")


pikkus = ""

for rida in fail:
    try:
        pikkus = 2/3*(float(rida)-2)
        print(round(pikkus))
        
    except:
        print("Vigane sisend!")

