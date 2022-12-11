from film import *

def töötleKäsk(käsk,järjend):
    if käsk=="K":
        print("Võimalikud filmid on:")
        filmid=loetleFilmid(järjend[0])
        for i in filmid:
            print(i)
    if käsk=="L":
        lisaFilm(" ".join(järjend[1:n]),järjend[0])
        print("Film lisatud!")
    if käsk=="V":
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        kustutaFilm(" ".join(järjend[0:n]))
    if käsk=="E":
        return("False")
    return("True")

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
while True:
    käsk=input()
    n=len(käsk)   
    käsk=käsk.split()
    if töötleKäsk(käsk[0],käsk[1:n]) == "False":
        break
