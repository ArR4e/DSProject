from film import *

def töötleKäsk(tähis,argumendid):
    while True:
        if tähis == "K":
            list = loetleFilmid(argumendid)
            print("Võimalikud filmid on: ")
            return True
        if tähis == "L":
            žanr,nimi = argumendid.split()
            lisaFilm(nimi,žanr)
            print("Film lisatud!")
            return True
        if tähis == "V":
            kustutaFilmid(argumendid)
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
            return True
        if tähis == "E":
            return False

print("Kuva filmid: K<žanr> \nLisa film:   L<žanr> <nimi> \nVaata filmi: V <nimi> \nLõpeta:      E")
        


        
        
        