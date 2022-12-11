from film import *

def töötleKäsk(käsk,järjend):
    if käsk=="K":
        print("Võimalikud filmid on:\n"+"\n".join(loetleFilmid(järjend[0])))
    if käsk=="L":
        lisaFilm(" ".join(järjend[1:]),järjend[0])
        print("Film lisatud!")
    if käsk=="V":
        kustutaFilm(" ".join(järjend[0:]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        
print("Kuva filmid: K <žanr>\nLisa film: L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta: E\n")

tõeväärtus=True
while tõeväärtus:
    sisend=input(">")
    if sisend=="E":
        tõeväärtus=False
    sisend.split()
    käsk=sisend[0]
    järjend=sisend[1:].split()  
    töötleKäsk(käsk,järjend)
    


   
    
