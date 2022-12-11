import math

def koogi_hind(nimi,moot): #pole täiesti kindel miks automaatkontroll faili viskab, endal töötab kui panna samad sisendid
    if sisestatud_nimi == "ploomikook" or sisestatud_nimi == "napoleoni kook" or sisestatud_nimi =="šokolaadikook":
        if nimi == "šokolaadikook":
            hind = round(((moot**2)*math.pi*0.06),2)
        elif nimi == "ploomikook":
            hind = round(((moot**2)*math.pi)*0.04,2)
        elif nimi == "napoleoni kook":
            hind = round((moot**2)*0.10,2)
        print ("Koogi maksumus on: ",hind) 
    else:
        raise Exception("Sellist kooki andmebaasis ei leitud")


while True:
    sisestatud_nimi = input("Sisesta koogi nimi:" ).lower()
    if sisestatud_nimi == "":
        break

    sisestatud_moot = float(input("Sisesta koogi mõõt: "))
    koogi_hind(sisestatud_nimi,sisestatud_moot)