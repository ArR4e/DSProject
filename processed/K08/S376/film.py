def filmid():
    filmid = []
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for rida in f:
            rida = rida.strip().split(" - ")
            filmid += [rida[0]]
   
    return filmid

def zanrid():
    zanrid = []
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for rida in f:
            rida = rida.strip().split(" - ")
            zanrid += [rida[1]]
   
    return zanrid

def loetleFilmid(zanr):
    sobivad_filmid = []
    indeks = 0
    
    for el in zanrid():
        indeks += 1
        if zanr == el:
            sobiv_film = [filmid()[indeks-1]]
            sobivad_filmid += sobiv_film
        else:
            continue
    
    return sobivad_filmid

def lisaFilm(nimi, zanr):
    sisu = ""
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for rida in f:
            if rida == "":
                continue
            else:
                sisu += rida
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        f.write(sisu)
        f.write("\n")
        f.write(nimi + " - " + zanr)
        
def kustutaFilm(nimi):
    sisu = ""
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for rida in f:
            if nimi in rida:
                continue
            if rida == "":
                continue
            else:
                sisu += rida
    
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        f.write(sisu)