from film import *

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        print(järjend[0] + "\n" + "Võimalikud filmid on:")
        a = loetleFilmid(järjend[0])
        for i in a:
            print(i)
    elif tähis == "L":
        if len(järjend) == 3:
            nimi = järjend[1] + " " + järjend[2]
        elif len(järjend) == 2:
            nimi = järjend[1]
        lisaFilm(nimi, järjend[0])
        print(järjend[0] + nimi + "\n" + "Film lisatud!")
    elif tähis == "V":
        if len(järjend) == 1:
            nimi = järjend[0]
        elif len(järjend) == 2:
            nimi = järjend[0] + " " + järjend[1]    
        kustutaFilm(nimi)
        print(nimi + "\n" + "Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
while True:
    kasklus = input("Sisesta käsklus: ")
    muutuja = kasklus.split()
    tähis = muutuja[0]
    if tähis == "K":
        järjend =  muutuja[1]
    elif tähis == "L":
        if len(muutuja) == 3:
            järjend = [muutuja[1]] + [muutuja[2]]
        elif len(muutuja) > 3:
            järjend = [muutuja[1]] + [muutuja[2]] + [muutuja[3]]
    elif tähis == "V":
        if len(muutuja) == 2:
            järjend = [muutuja[1]]
        elif len(muutuja) == 3:
            järjend = [muutuja[1]] + [muutuja[2]]
    if tähis == "E":
        break
    töötleKäsk(tähis, järjend) 
    
    