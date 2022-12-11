from film import *

def töötleKäsk(tähis,järjend):
    if tähis == "K":
        print(f"Võimalikud filmid on: {loetleFilmid(teine)}")
    if tähis == "L":
        lisaFilm(kolmas, teine)
        print(f"Film lisatud!")
    if tähis == "V":
        kustutaFilm(teine)
        print(f"Fail nimekirjast kustutatud!")

while True:
    print(f"=== FILMIANDBMEBAAS ===\nKuva filmid: K <zanr>\nLisa film:   L <zanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===") 
    sisend = input("Sisesta käsud: ")
    esimene = (sisend.strip(" ").split(" "))[0]
    if esimene == "K":
        töötleKäsk(esimene, teine)
        teine = (sisend.strip(" ").split(" "))[1]
    if esimene == "L":
        töötleKäsk(esimene, [teine, kolmas])
        teine = (sisend.strip(" ").split(" "))[1]
        kolmas = (sisend.strip(" ").split(" "))[2:len(sisend)]
    if esimene == "V":
        teine = (sisend.strip(" ").split(" "))[1]
        töötleKäsk(esimene, [teine])   
    if esimene == "E":
        break