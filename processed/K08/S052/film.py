def loetleFilmid(žanr):
    f = open("filmid.txt",encoding="UTF-8")
    filmid = []
    
    for i in f:
        if žanr in i.strip():
            film = i.strip()[0:(len(i.strip())-len(žanr)-3)]
            filmid.append(film)
    return filmid
    f.close()



def lisaFilm(nimi, žanr):
    with open("filmid.txt",mode="a",encoding="UTF-8") as f:
        rida = "\n" + str(nimi) + " - " + str(žanr)
        f.write(rida)
        f.close()



def kustutaFilm(nimi):   
    a = 0
    read = []
    f = open("filmid.txt",mode="r+",encoding="UTF-8")
    
    for i in f:
        if not nimi in i.strip():
            read.append(i)
    f.truncate(0) #tühjendab faili
    f.close()
    
    ridade_arv = len(read)
    
    with open("filmid.txt",mode="a",encoding="UTF-8") as f:
        while a < ridade_arv:
            f.write(read[a])
            a += 1
