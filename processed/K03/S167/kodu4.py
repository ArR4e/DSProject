#Erindite püüdmine failist lugemisel
#jalalabapikkus=int((2/3)*(kinganumber-2))

#prooviks whilega võtta kogu failisisu, mille read on eraldatud. Ehk siis while looks erinevad muutujad.
f = open("kinganumbrid.txt", "r")

while True:
    rida = f.readline().strip()
    try:
        if rida == "":
            break
        kinganr = float(rida.strip())
        jalanumber = float((2/3)*(kinganr-2))
        jalanumber2 = int(round(jalanumber))
        c=str(jalanumber2)
        print(c)
    except ValueError:
        a = print("Vigane sisend")
#    if rida.isnumeric() or c.isnumeric() == True:
#        print(c)
#    else: print("Vigane sisend")

