def loetleFilmid(t):
    f = open("filmid.txt", "r", encoding="utf-8")
    loetletud = []
    filmid = f.readlines()
    for i in filmid:
        if t in i:
            loetletud.append(i.split(" - ")[0]) 
    return(loetletud)
    f.close()

    
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a+", encoding="utf-8")
    f.write("\n"+nimi+" - "+žanr)
    f.close()



def kustutaFilm(nimi):
    f = open("filmid.txt", "a+", encoding="utf-8")
    f.seek(0)
    filmidk = f.readlines()
    f.truncate(0)
    f.close()
    f = open("filmid.txt", "a+", encoding="utf-8")
    f.seek(0)
    for i in filmidk:
        if nimi not in i:
            f.write(i)
    f.close()
    
