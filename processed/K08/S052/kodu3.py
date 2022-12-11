from film import lisaFilm
from film import loetleFilmid
from film import kustutaFilm

print("=== FILMIANDMEBAAS === \n Kuva filmid: K <žanr> \n Lisa film:   L <žanr> <film> \n Vaata filmi: V <filmi nimi> \n Lõpeta:      E \n ===")

def töötleKäsk(käsk, argumendid):
        if " " in argumendid and käsk != "K" and käsk != "V":
            argumendid_list = argumendid.split(" ", 1)
            žanr = argumendid_list[0]
            nimi = argumendid_list[1]
            lisaFilm(nimi, žanr)
            print("Film lisatud!")
            
        else:
            if käsk == "K":
                žanr = argumendid
                print("Võimalikud filmid on: ")
                loetleFilmid(str(žanr))
            elif käsk == "V":
                nimi = argumendid
                kustutaFilm(nimi)
                print("Film nimekirjast kustutatud! \n Head vaatamist!")
                
def false():
    return False

while True:           
    sisend = input()
    sisend_list = sisend.split(" ",1)
    käsk = sisend_list[0]
    if sisend == "E":
        false()
        break
    argumendid = sisend_list[1]
    töötleKäsk(käsk, argumendid)

