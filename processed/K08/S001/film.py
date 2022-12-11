def loetleFilmid(zanr):
    filmid = open("filmid.txt", "r", encoding="utf-8")
    nimekiri = []
    for film in filmid:
        film = film.strip()
        film = film.split(" - ")
        if film[1] == zanr:
            nimekiri.append(film[0])
    filmid.close()
    return nimekiri

def lisaFilm(nimi,zanr):
    filmid = open("filmid.txt", "a", encoding="utf-8")
    filmid.write("\n" + nimi + " - " + zanr)
    filmid.close()
    
def kustutaFilm(nimi):
    filmid_vana = open("filmid.txt", "r", encoding="utf-8")
    nimed = []
    zanrid = []
    for film in filmid_vana:
        film = film.strip()
        film = film.split(" - ")
        if film[0] == nimi or film == [""]:
            continue
        nimed.append(film[0])
        zanrid.append(film[1])
    filmid_vana.close()
    filmid_uus = open("filmid.txt", "w", encoding="utf-8")
    for a in range(0,len(nimed)):
         filmid_uus.write(nimed[a] + " - " + zanrid[a] + "\n")
    filmid_uus.close()

