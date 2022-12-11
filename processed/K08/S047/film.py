"""f = open("filmid.txt", encoding="UTF-8")
read = f.readlines()
f.close()

nimed = []
zanrid = []

for rida in read:
    rida = rida.strip()
    tükid = rida.split(" - ")
    nimed += [tükid[0]]
    zanrid += [tükid[1]]
"""

def loetleFilmid(zanr):
    f = open("filmid.txt", encoding="UTF-8")
    read = f.readlines()
    f.close()

    loetle=[]
    for rida in read:
        rida = rida.strip()
        tükid = rida.split(" - ")
        
        if zanr == tükid[1]:
             loetle += [tükid[0]]  
    return loetle

def lisaFilm(nimi, zanr):
    f=open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()


def kustutaFilm(nimi):
    f = open("filmid.txt","r")
    read = f.readlines()
    f.close()

    nimi_tükis=" ".join(nimi)
    f = open("filmid.txt", "w")
    for rida in read:
        rida = rida.strip()
        tükid = rida.split(" - ")
        
        if nimi_tükis != tükid[0]:
            f.write(rida+"\n")
    f.close()