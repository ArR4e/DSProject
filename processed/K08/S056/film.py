filmid = []
loetud_žanrid = []
õiged_filmid = []
#See suudab ainult ühe filmi tuvastada järjendist mis sobib ja tagastab selle
def loetleFilmid(žanr):
    fail = open("filmid.txt", encoding = "UTF-8")
    for rida in fail:
        film_ja_žanr = rida.split(" - ")
        film = film_ja_žanr[0]
        loetud_žanr = film_ja_žanr[1]
        filmid.append(film)
        loetud_žanr_1 = loetud_žanr.strip()
        loetud_žanrid.append(loetud_žanr_1)
    i = loetud_žanrid.index(žanr)
    õige_film = filmid[i]
    õiged_filmid.append(õige_film)
    return õiged_filmid


def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding = "UTF-8")
    fail.write("\n" + nimi + " - " + žanr)
    fail.close()

def kustutaFilm(nimi):
#fail avada, lugeda sisse, siis kinni. Siis uuesti avada (kirjutamiseks), teha see muudatus ja siis kirjutada uude faili
    fail = open("filmid.txt", encoding = "UTF-8")
    while True:
        rida = fail.readline()
        if rida == " ":
            break
    fail.close()