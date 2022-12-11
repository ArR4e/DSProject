from film import *

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        print("Võimalikud filmid on:")
        for filmm in loetleFilmid(järjend[0]):
            print(filmm)
        return True
    elif tähis == "L":
        žanr = järjend[0]
        filminimi = ""
        for sõna in järjend:
            if sõna != žanr:
                filminimi+=sõna+" "
        filminimi = filminimi[:-1]
        lisaFilm(filminimi, žanr)
        print("Film lisatud!")
        return True
    elif tähis == "V":
        filminimi = ""
        for sõna in järjend:
            filminimi+=sõna+" "
        filminimi = filminimi[:-1]
        kustutaFilm(filminimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    elif tähis == "E":
        return False
    
sisend = input("").split(" ")
tähis = sisend[0]
järjend = []
del sisend[0]
for element in sisend:
    järjend.append(element)

while töötleKäsk(tähis, järjend) == True:
    sisend = input("").split(" ")
    tähis = sisend[0]
    järjend = []
    del sisend[0]
    for element in sisend:
        järjend.append(element)