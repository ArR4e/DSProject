from film import *

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")

def töötleKäsk(täht, x):
    täht = täht.lower()
    if täht == "k":
        print("Võimalikud filmid on: ")
        žanr = x[0]
        järjend = loetleFilmid(žanr.lower())
        if järjend == []:
            print("Tekstifailis pole soovitud žanrist")
            return True
        for i in järjend:
            print(i)
        return True
    elif täht == "l":
        nimi = " ".join(x[1:])
        lisaFilm(nimi, x[0])
        print("Film lisatud!")
        return True
    elif täht == "v":
        nimi = " ".join(x)
        kustutaFilm(nimi)
        print("""Film nimekirjast kustutatud!
Head vaatamist!""")
        return True
    elif täht == "e":
        return False;
while True:
        sisend = input()
        x = []
        x += (sisend[2:].split(" "))
        if not töötleKäsk(sisend[0], x):
            break
    