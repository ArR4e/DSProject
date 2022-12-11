fail = open("Kinganumbrid.txt")
while True:
    try:
        rida = fail.readline().strip()
        if rida == "":
            break
        rida1 = float(rida)
        pikkus = 2/3 *(rida1 - 2)
        pikkus1 = round(pikkus)
        print(pikkus1)
    except:
        print("Vigane sisend")
    
    