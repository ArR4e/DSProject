from film import loetleFilmid 
from film import lisaFilm
from film import kustutaFilm

def töötleKäsk(käsk, argumendid):
    if käsk == "K":
        filmid_z = loetleFilmid(argumendid[0])
        if len(filmid_z) > 0: 
            print("Võimalikud filmid on:")
            for filmi_nimi in filmid_z:
                print (filmi_nimi)
            return True
        else:
            print("Vastet ei leitud!")
    elif käsk == "L":
        z = argumendid[0]
        del argumendid[0]
        filmi_nimi = " ".join(argumendid)
        lisaFilm(filmi_nimi, z)
        print("Film lisatud!")
        return True
    elif käsk == "V":
        filmi_nimi = " ".join(argumendid)
        kustutaFilm(filmi_nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    elif käsk == "E":
        return False
    else:
        return False

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")


while True:
    käsk = input("")

    käsu_elemendid = käsk.split(" ")
    käsu_täht = käsu_elemendid[0]

    del käsu_elemendid[0]

    vastus = töötleKäsk(käsu_täht, käsu_elemendid)
    if vastus == False:
        break

    