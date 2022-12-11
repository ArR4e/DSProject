from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
def töötleKäsk(a, b):
    if a == "K":
        järjend = loetleFilmid(b)
        print("Võimalikud filmid on:")
        for i in järjend:
            print(i)
    if a == "L":
        nimi = abuus[1]
        žanr = abuus[2]
        lisaFilm(žanr, nimi)
        print("Film lisatud!")
    if a == "V":
        abuuss = ab.split(" ", 1)
        kustutaFilm(abuuss[1])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    if a == "E":
        return False
while True:
    ab = str(input(""))
    abuus = ab.split(" ", 2)
    a = abuus[0]
    try:
        b = abuus[1]
    except:
        break
    tühi = []
    if töötleKäsk(a, b) == False:
        break