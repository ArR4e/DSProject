from film import *

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        print("Võimalikud filmid on:")
        for film in loetleFilmid(järjend[0]):
            print(film)
    if käsk == "L":
        nimi = " ".join(järjend[1:])
        lisaFilm(nimi, järjend[0])
        print("Film lisatud!")
    if käsk == "V":
        nimi = " ".join(järjend)
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    if käsk == "E":
        return False
    return True

while True:
    sisend = input("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===").split()
    käsk = sisend[0]
    järjend = sisend[1:]
    #print(järjend)
    if töötleKäsk(käsk, järjend) == False:
        break