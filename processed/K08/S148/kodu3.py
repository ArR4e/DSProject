from film import *

def töötleKäsk(tähis, järjend):
    while True:
        if tähis == "K":
            if loetleFilmid(järjend[0]) != []:
                print(loetleFilmid(järjend[0]))
            else:
                print("Selle žanri alt filme ei leitud.")
            return True
        
        elif tähis == "L":
            lisaFilm(järjend[1], järjend[0]) # järjendi probleem
            print("Film lisatud!")
            return True
        
        elif tähis == "V":
            kustutaFilm(järjend[0]) # samuti järjendi probleem
            print("Film nimekirjast kustutatud!\nHead vaatamist!")
            return True
        
        elif tähis == "E":
            return False
        
        else:
            return True

print("Kuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E")

sisend1 = input("> ")
sisend2 = sisend1.split(" ")

while töötleKäsk(sisend2[0], sisend2[1:]) == True:
    sisend1 = input("> ")
    sisend2 = sisend1.split(" ")