import film
print("""
o________Filmiandmebaas________o
| kuva filmid: K <žanr>        |
| lisa film  : L <žanr> <nimi> |
| vaata filmi: V <nimi>        |
| lõpeta     : E               |
o______________________________o
""")
def töötleKäsk(sisend):
    täht = sisend.split()[0]
    if täht == "K":
        nimekiri = film.loetleFilmid(sisend[2:])
        if nimekiri != []:
            print("Võimalikud filmid on:\n"+("\n".join(nimekiri)))
        return True
    elif täht == "L":
        žanr = sisend.split()[1]
        nimi = " ".join(sisend.split()[2:])
        film.lisaFilm(nimi,žanr)
        print(f"Edukalt lisatud film {nimi} žanriga {žanr}.")
        return True
    elif täht == "V":
        nimi = sisend[2:]
        film.kustutaFilm(nimi)
        return True
    elif täht == "E":
        return False
    else:
        print("Sellist käsku ei leitud, palun proovige uuesti.")
        return True
while True:
    tulemus = töötleKäsk(input())
    if tulemus == False:
        break