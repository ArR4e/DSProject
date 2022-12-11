from film import *

algus = input("---- FILMIANDMEBAAS ----\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n---- \n")
valikud = algus.split(" ")
tähistus = valikud[0]
filmivalik = valikud[1:]

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        a = loetleFilmid(järjend[0])
        if a!= []:
            print("Võimalikud filmid on: \n" + "\n".join(a))
        else:
            print("Valitud žanr puudub. Proovige uuesti")
        return True
    elif tähis == "L":
        lisaFilm(" ".join(järjend[1:]), järjend[0])
        print("Film lisatud!")
        return True
    elif tähis == "V":
        kustutaFilm(" ".join(järjend))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif tähis == "E":
        return False
    else:
        print("Ebasobiv sisend, proovige uuesti")
        return True

while töötleKäsk(tähistus, filmivalik) == True:
    tava = input()
    valikud = tava.split(" ")
    tähistus = valikud[0]
    filmivalik = valikud[1:]
    continue