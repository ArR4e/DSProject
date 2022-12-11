def loetleFilmid(žanr):
    f=open("filmid.txt", "r", encoding="UTF-8")
    nimed=[]
    for rida in f.readlines():
        if žanr in rida:
            nimed.append(rida.split(" - ")[0])
    f.close()
    return nimed

def lisaFilm(nimi, žanr):
    f=open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n"+nimi+" - "+žanr)
    f.close()
    
def kustutaFilm(nimi):
    f=open("filmid.txt", "r", encoding="UTF-8")
    järel=""
    for rida in f.readlines():
        if not nimi in rida:
            järel+=rida
    f.close()
    f=open("filmid.txt", "w", encoding="UTF-8")
    f.write(järel)
    f.close()