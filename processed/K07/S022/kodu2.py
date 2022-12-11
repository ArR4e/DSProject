#tee = float(input("Sisesta tee pikkus kilomeetrites "))
def taksosoit(tee):
    takso = open("taksohinnad.txt", "r")
    n = 0
    hind = 0
    nimi = ""
    while True:
        firma = takso.readline()
        if firma =="":
            break
        firma = firma.strip()
        firmaand = list(firma.split(","))
        for el in firmaand:
            if n == 0:
                nimi1 = el
                n = n + 1
                continue
            if n == 1:
                el = float(el)
                sisse = el
                n = n + 1
                continue
            if n == 2:
                el = float(el)
                sõit = el
                n = 0
            hind1 = sisse + sõit * tee
            if hind == 0:
                hind = hind1
                nimi = nimi1
            elif hind1 < hind:
                hind = hind1
                nimi = nimi1
            break
    return nimi
    
tee = float(input("Sisesta tee pikkus kilomeetrites: "))
print("Odavaim firma on", taksosoit(tee))