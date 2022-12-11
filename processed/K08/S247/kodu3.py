from film import *

def töötleKäsk(käsk, argumendid):
    while True:
        if käsk == "K":
            a = loetleFilmid(argumendid)
            print("Võimalikud filmid on: ")
            for el in a:
                print(el)
            return True
        if käsk == "L":
            žanr, nimi = argumendid.split(" ",1)
            lisaFilm(nimi, žanr)
            print("Film lisatud!")
            return True
        if käsk == "V":
            kustutaFilm(argumendid)
            print("Film nimekirjast kustutatud!", "Head vaatamist!", sep=("\n"))
            return True
        if käsk == "E":
            return False
            
print("Kuva filmid: <žanr> \nLisa film:   L <žanr> <filmi nimi> \nVaata filmi: V <filmi nimi> \nLõpeta:      E")

sisend = input()
käsk = sisend[0]
sisend = sisend[1::]
argumendid = sisend.strip()

while True:
    töötleKäsk(käsk, argumendid)
    sisend = input()
    käsk = sisend[0]
    if käsk == "E":
        break
    else:
        sisend = sisend[1::]
        argumendid = sisend.strip()
        


            