f1 = open("lapsed.txt")
f2 = open("nimed.txt")

isic_sõnastik = {}
for i in f1:
    lapsevanem = i.split()[0]
    laps = i.split()[1]
    isic_sõnastik[laps]=lapsevanem
    
f1.close()

nimed_sõnastik = {}
for i in f2:
    isic = i.split()[0]
    nimi = i.split()[1]
    perenimi = i.split()[2]
    nimed_sõnastik[nimi +" "+ perenimi]=isic

f2.close()

#isic_sõnastik(laps) panen võrduma nimi_sõnastik(isic) tagasta nimi_sõnastik(nimi, perenimi)
#pärast returnin nagu töölehes.

