from film import *

def töötleKäsk(tähis,järjend):
            
        if tähis=="K":
            žanr = järjend
            print("võimalikud filmid on:", loetleFilmid(žanr))
        elif tähis=="L":
            k=(järjend.split(" "))[0]
            n=(järjend.split(" "))[1]
            lisaFilm(n,k)
            print("Film lisatud!!")
        elif tähis=="V":
            print(järjend)
            kustutaFilm(järjend)
            print("film on nimekirjast kustutatud!")
        
while True:
    i=input()
    k=i.split(" ")
    if i=="E":
        break
    elif k[0]=="K":
        töötleKäsk("K",str(k[1]))
    elif k[0]=="L":
        del k[0]
        töötleKäsk("L", str(" ".join(k)))
    elif k[0]=="V":
        del k[0]
        töötleKäsk("V",str(" ".join(k)))