from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm

print("=== FILMIANDMEBAAS ===")
k = input("Kuva filmid: ")
k = k.split()
l = input("Lisa film: ")
l = l.split()
v = input("Vaata filmi: ")
v = v.split()
e = input("Lõpeta: ")
if k[0] == "K":
    print("Võimalikud filmid:", loetleFilmid(k[1]))  
if l[0] == "L":
    lisaFilm(l[2], l[1])
    print("Film lisatud!")
if v[0] == "V":
    kustutaFilm(v[0])
    print("Film nimekirjast kustutatud!")
    print("Head vaatamist!")
while e == "E":
    break