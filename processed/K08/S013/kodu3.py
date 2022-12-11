import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        sann = järjend[0]
        print(("Võimalikud filmid on: ") + str(film.loetleFilmid(sann)))
        return True
    elif tähis == "L":
        sann = järjend[0]
        film.lisaFilm(" ".join(z), sann)
        print("Film lisatud")
        return True
    elif tähis == "V":
        kustutamine = järjend[1: len(järjend)]
        film.kustutaFilm(" ".join(kustutamine))
        print("Film nimekirjast kustutatud!\n Head vaatamist!")
        return True
    elif tähis == "E":
        return False
        

print("=== FILMIANDMEBAAS ===\n Kuva filmid: K <žanr>\n Lisa film:   L <žanr> <film>\n Vaata filmi: V <filmi nimi>\n Lõpeta:      E\n ===")

x = input().split()
järjend = x
y = järjend[0]
z = järjend[1: len(järjend)]

while töötleKäsk(y, z) == True:
    x = input().split()
    järjend = x
    y = järjend[0]
    z = järjend[1: len(järjend)]
    