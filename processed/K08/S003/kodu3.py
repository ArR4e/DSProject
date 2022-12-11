from film import *

def töötleKäsk(tähis,järjend=[]):
    if tähis == "K":
        filmid = loetleFilmid(järjend[0])
        print("võimalikud filmid on!")
        for el in filmid:
            print(el)
        return True
    elif tähis == "L":
        lisaFilm(järjend[1],järjend[0])
        print("Film lisatud!")
        return True
    elif tähis == "V":
        kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    elif tähis == "E":
        return False
    else:
        print("Vale käsk!")
töötab = True

while töötab:
    sisend = input()
    sisendi_osad = sisend.split(" ",1)
    tähis = sisendi_osad[0]
    if len(sisendi_osad) > 1:
        sisendi_osad = sisendi_osad[1].split(" ",1)
    töötab = töötleKäsk(tähis,sisendi_osad)
    