from film import *

def töötleKäsk(käsk, järjend=[]):
    if käsk == "E":
        return False
    
    elif käsk == "K":
        print("Võimalikud filmid on: ")
        filmid = loetleFilmid(järjend[0])
        for i in filmid:
            print(i)
        return True
    
    elif käsk == "L":
        zanr = järjend[0]
        järjend.remove(zanr)
        film = " ".join(järjend)
        lisaFilm(film, zanr)
        print("Film lisatud!")
        return True
    
    elif käsk == "V":
        film = " ".join(järjend)
        kustutaFilm(film)
        print("Head vaatamist!")
        return True
    
    else:
        print("Sellist käsku andmebaasis ei ole!")
        return True
 
print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")

while True:
    sisend = input()
    järjend = sisend.split()
    käsk = järjend[0]
    järjend.remove(käsk)
    if töötleKäsk(käsk, järjend) == False:
        break
