from film import *

def töötleKäsk(tähis, järjend):
    if tähis=="K":
        print("Võimalikud filmid on:")
        for nimi in loetleFilmid(järjend[0]):
            print(nimi)
    elif tähis=="L":
        lisaFilm(järjend.split(" ",1)[1], järjend.split(" ", 1)[0])
        print("Film lisatud!")
    elif tähis=="V":
        kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
    elif tähis=="E":
        return False
    return True

käsk=input()
while käsk != "E":
    terve=käsk.split(" ", 1)
    töötleKäsk(terve[0], terve[1])
    käsk=input()