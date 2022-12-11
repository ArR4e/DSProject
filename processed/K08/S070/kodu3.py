from film import *

def töötleKäsk(käsk, info):
    if käsk == "K":
        zanr = info
        print("Võimalikud filmid on:")
        nimekiri = loetleFilmid(zanr)
        for l in range(len(nimekiri)):
            print(nimekiri[l])
        return True
    if käsk == "L":
        rida = info.split(" ", 1)
        nimi = rida[1]
        tüüp = rida[0]
        lisaFilm(nimi, tüüp)
        print("Film lisatud!")
        return True
    if käsk == "V":
        nimi = info
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        return True
    if käsk == "E":
        return False


print("=== FILMIANDMEBAAS ===\nKuvafilmid: K -žanr-\nLisa film: N -žanr- -film-\nVaata filmi: V -filmi nimi-\nLõpeta: E\n\n\n\n")
while True:
    in_put = input(">")
    in_put = in_put.split(" ", 1)
    if len(in_put) < 2:
        in_put.append("x")
    if töötleKäsk(in_put[0], in_put[1]) == False:
        break