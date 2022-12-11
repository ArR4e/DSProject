import film

def töötleKäsk(käsk,järjend):
    if käsk == "K":
        filmid = film.loetleFilmid(järjend[0])
        print("Võimalikud filmid on:")
        print("\n".join(filmid))
    if käsk == "L":
        nimi = (" ".join(järjend[1:]))
        print(nimi)
        film.lisaFilm(nimi,järjend[0])
        print("Film lisatud.")
    if käsk == "V":
        film.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
    if käsk == "E":
        return False
    return True

while True:
    käsu_tähis = input("")
    sisend = []
    sisend += käsu_tähis.split(" ")
    käsk = sisend[0]
    järjend = sisend[1:]
    if töötleKäsk(käsk,järjend) == True:
        continue
    else:
        break
