def loetleFilmid(žanrinimed):
    i = 0
    valik = []
    while i < len(žanrid):
        if žanrinimed in žanrid[i]:
            valik.append(nimed[i])
        i += 1
    return valik

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "a", encoding="UTF-8") as f:
        print(nimi, "-", žanr, f)
    return "Film lisatud!"

def kustutaFilm(nimi):
    x = 0
    with open("filmid.txt", encoding="UTF-8") as f:
        fread = f.readlines()
        muutus = []
        for el in fread:
            muutus.append(el.strip())
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        for rida in muutus:
            if nimi not in muutus[x]:
                f.write(rida)
                f.write("\n")
            x += 1
    return "Film kustutatud!"

with open("filmid.txt", encoding="UTF-8") as f:
    nimed = []
    žanrid = []
    for rida in f:
        osadeks = rida.split(" - ")
        nimed.append(osadeks[0].strip())
        žanrid.append(osadeks[1].strip())


    
    