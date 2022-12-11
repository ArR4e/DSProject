def loetleFilmid(žanr):
    filmid_žanrid = open("filmid.txt")
    if žanr == "märul":
        while True:
            rida = filmid_žanrid.readline()
            märul = "märul" in rida
            if märul == True:
                märulifilm = [rida.split(" - ", 1)[0]]
                return märulifilm
    elif žanr == "multikas":
        while True:
            rida = filmid_žanrid.readline()
            multikas = "multikas" in rida
            if multikas == True:
                multifilm = [rida.split(" - ", 1)[0]]
                return multifilm
    elif žanr == "õudukas":
        while True:
            rida = filmid_žanrid.readline()
            õudukas = "õudukas" in rida
            if õudukas == True:
                õudusfilm = [rida.split(" - ", 1)[0]]
                return õudusfilm
    filmid_žanrid.close()
                
def lisaFilm(nimi, žanr):
    filmid_lisamiseks = open("filmid.txt", "a")
    uus_film = "\n" + nimi + " - " + žanr
    filmid.write(uus_film)
    filmid.close()
    
def kustutaFilm(film):
    filmid_kustutamiseks = open("filmid.txt", "r+")
    for rida in filmid_kustutamiseks:
        filminimi = rida.split(" - ", 1)[0]