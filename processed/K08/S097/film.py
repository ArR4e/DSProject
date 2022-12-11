def loetleFilmid(žanr):
    filmiLoetelu = []
    f = open("filmid.txt", encoding = "UTF-8")
    for rida in f:
        ridaJärjendina = list(rida.strip("\n").split(" - "))
        if žanr in ridaJärjendina:
            film = ridaJärjendina[0]
            filmiLoetelu = filmiLoetelu + [film]
        else:
            continue
    return filmiLoetelu
    f.close()
            
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
    
def kustutaFilm(nimi):      
    with open("filmid.txt", encoding = "UTF-8") as f:
        uussisu = ""
        for rida in f:
            ridaJärjendina = list(rida.split(" - "))
            if nimi in ridaJärjendina:
                continue
            else:
                uussisu = uussisu + rida
    with open("filmid.txt", "w", encoding = "UTF-8") as g:
        g.write(uussisu)
