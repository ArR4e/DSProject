def loetleFilmid(žanr):
    f=open("filmid.txt", encoding="utf=8")
    valik=[]
    for read in f:
        eraldus = read.strip()
        järjend = eraldus.split(" - ")
        
        filminimed=järjend[0]
        
        žanrid=järjend[-1]
        
        if žanrid == žanr:
            valik.append(filminimed)
    return valik            
    f.close()

def lisaFilm(nimi, žanr):
    f=open("filmid.txt", "a", encoding="utf=8")
    uusrida= "\n" + nimi + " - " + žanr
    f.write(uusrida)
    f.close()
    return

def kustutaFilm(nimi):
    with open("filmid.txt", encoding="utf=8") as algne:
        read=algne.readlines()
    with open("filmid.txt", "w", encoding="utf=8") as lõpp:
        for rida in read:
            if nimi not in rida.strip("\n"):
                lõpp.write(rida)
    algne.close()
    lõpp.close()