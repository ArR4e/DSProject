fail = open("Kinganumbrid.txt")

while True:
    try:
        rida = fail.readline()
        if rida == "":
           break
        x = float(rida)
        pikkus = 2/3 * (x - 2)
        y = round(pikkus)
        print(y)
    
    except:
        print( "Vigane sisend " )