fail = open("taksohinnad.txt", encoding = "UTF-8")
teepikkus = float(input("Sisestage tee pikkus kilomeetrites: "))

odavaim = ""
hind = 0

for rida in fail:
    tekst = rida.split(",")
    
    nimi = tekst[0]
    istumine = float(tekst[1])
    kilomeeter = float(tekst[2])
    
    sõidu_hind = istumine + (kilomeeter*teepikkus)
    
    if hind == 0:
        hind = sõidu_hind
        odavaim = nimi
    elif sõidu_hind < hind:
        hind = sõidu_hind
        odavaim = nimi

print("Odavaim on", odavaim)