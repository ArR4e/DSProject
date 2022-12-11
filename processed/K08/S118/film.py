
def loetleFilmid(žanr):
    fail = open("filmid.txt", "r", encoding="utf-8")

    filmid = fail.readlines()

    filminimed = []
    žanrid = []

    for rida in filmid:
        if rida != "\n":
            film = rida.split(" - ")[0]
            žanrlisa = rida.split(" - ")[1].replace("\n","")
            filminimed.append(film)
            žanrid.append(žanrlisa)
    
    fail.close()
    valitudFilmid = []
    for number in range(0, len(žanrid)):
        if žanrid[number] == žanr:
            valitudFilmid.append(filminimed[number])
    return valitudFilmid

def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding="utf-8")
    fail.write("\n"+nimi+" - "+žanr)
    fail.close()
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r", encoding="utf-8")

    filmid = fail.readlines()

    filminimed = []
    žanrid = []

    for rida in filmid:
        if rida != "\n":
            film = rida.split(" - ")[0]
            žanr = rida.split(" - ")[1].replace("\n","")
            filminimed.append(film)
            žanrid.append(žanr)
    
    fail.close()
    fail = open("filmid.txt", "w", encoding="utf-8")
    for number in range(0, len(filminimed)):
        if filminimed[number] != nimi:
            fail.write("\n"+filminimed[number]+" - "+žanrid[number])
