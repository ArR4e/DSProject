teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim = ""
koguhind = 0.0
odavaimhind = 0.0
with open("taksohinnad.txt") as f:
    for rida in f.readlines():
        reas = rida.strip().split(",")
        nimi = reas[0]
        sisseastumine = float(reas[1])
        kmhind = float(reas[2])
        koguhind = sisseastumine + teepikkus*kmhind
        if koguhind < odavaimhind or odavaimhind == 0:
            odavaim = nimi
            odavaimhind = koguhind
print(f"Kõige odavam on {odavaim}")