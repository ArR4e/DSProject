from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
def töötleKäsk(a, järjend):
    if a == "K":
        d = loetleFilmid(järjend)
        print("Võimalikud filmid on: ")
        for x in range(len(d)):
            print(d[x])
        d.clear()
    elif a == "L":
        zanr = c[2]
        lisaFilm(järjend, zanr)
        print("Film lisatud!")
    elif a == "V":
        kustutaFilm(järjend)
        print("Film nimekirjast kustutatud")
    elif a == "E":
        print("")
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===")
while True:
    b = input()
    if b == "E":
        break
    c = b.split()
    töötleKäsk(c[0], c[1])
    continue