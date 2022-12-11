# 3. Juku filmiandmebaas / RP

from film import *

print("""====== FILMIANDMEBAAS ======
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
============================
""")

def töötleKäsk(tähis, järjend):
    while True:
        tähis = input("")
        nimi = ""
        if tähis[0] in järjend:
            tähis = tähis.split(" ")
            if tähis[0] == "K":
                if len(loetleFilmid(tähis[1])) > 0:
                    print("Võimalikud filmid on:")
                    for el in loetleFilmid(tähis[1]):
                        print(el)
                else:
                    print("Sellist zanrit ei leitud, proovige uuesti!")
            if tähis[0] == "L":
                tick = 1
                for el in tähis[2:]:
                    if tick != len(tähis[2:]):
                        nimi += el + " "
                    else:
                        nimi += el
                    tick += 1
                lisaFilm(nimi, tähis[1])
                print("Film lisatud!")
            if tähis[0] == "V":
                tick = 1
                for el in tähis[1:]:
                    if tick != len(tähis) - 1:
                        nimi += el + " "
                    else:
                        nimi += el
                    tick += 1
                kustutaFilm(nimi)
                print("Film nimekirjast kustutatud!")
                print("Head vaatamist!")
            if tähis[0] == "E":
                return False
 

töötleKäsk("", ["K","L","V","E"])