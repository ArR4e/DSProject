from math import pi

def koogi_hind(koogi_nimi, koogi_moot):
    if koogi_nimi!= "šokolaadikook" and koogi_nimi!= "ploomikook" and koogi_nimi!= "Napoleoni kook":
        raise Exception ('Sellist kooki andmebaasist ei leitud')
    
    if koogi_nimi== "Napoleoni kook":
        S=pow(koogi_moot, 2)
        return round(S*0.1,2)
    else:
        S=pow(koogi_moot, 2)*pi
        if koogi_nimi=="šokolaadikook":
            return round(S*0.06, 2)
        else:
            return round(S*0.04, 2)
while True:       
    nimi=input('Sisestage soovitud koogi nimi: ')
    if nimi=='':
        break
    else:
        moot=float(input('Sisestage koogi moot: '))
        print(koogi_hind(nimi, moot))
