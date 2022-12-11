from film import *
a = 1
print("=== FILMIANDMEBAAS === \n\
Kuva filmid: K <žanr> \n\
Lisa film:   L <žanr> <film> \n\
Vaata filmi: V <filmi nimi> \n\
Lõpeta:      E")
while a == 1:
    b = str(input("")).split(" ")
    if b[0] == "K":
        print(loetleFilmid(b[1]))
    elif b[0] == "L":
        lisaFilm(b[2],b[1])
    elif b[0] == "V":
        kustutaFilm(b[1])
    elif b[0] == "E":
        a = 0