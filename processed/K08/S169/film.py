def loetleFilmid(zanr):
    list = []
    f = open("filmid.txt","r",encoding="utf8")
    for a in f.readlines():
        if a.split("-")[-1].strip() == zanr:
            list.append(a.split(" - ")[0].strip())
    f.close()
    return list
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt","a",encoding="utf8")
    f.write("\n")
    f.write(nimi + " - " + zanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt","r",encoding="utf-8")
    list = f.readlines()
    f.close()
    f2 = open("filmid.txt","w",encoding="utf-8")
    for a in list:
        if a.split("-")[0].strip() != nimi:
            f2.write(a)
    f2.close()
            