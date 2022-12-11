f = open("kinganumbrid.txt")


while True:
    try:
        rida = f.readline().strip()
        if rida == "":
            break
        print(round((2/3) * (float(rida) - 2)))    
    except:
        print("Vigane sisend")

f.close()