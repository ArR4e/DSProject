f=open("kinganumbrid.txt", encoding='UTF-8')
pikkus=0

for rida in f:
    try:
        rida = rida.strip()
        #print(rida)
        if ("*" not in rida and " " not in rida) and type(float(rida))==float:
            pikkus = round(2/3 * (float(rida) - 2))
            print(str(pikkus))
        else:
            print("Vigane sisend")
    except:
        print("Vigane sisend")
f.close()