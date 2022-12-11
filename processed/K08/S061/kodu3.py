from film import *
def töötleKäsk(tahis, jarjend):
    if tahis == "K":
        filmid = loetleFilmid(jarjend[0])
        print(tahis + " " + jarjend[0] + "\n" + "Võimalikud filmid on:")
        for film in filmid:
            print(film)
    elif tahis == "L":
        if len(jarjend) > 2:
            film = jarjend[1] + " " + jarjend[2]
        else:
            film = jarjend[1]
        lisaFilm(film, jarjend[0])
        print(tahis + " " + jarjend[0] + " " +  film + "\n" + "Film lisatud!")
    elif tahis == "V":
        if len(jarjend) > 1:
            film = jarjend[0] + " " + jarjend[1]
        else:
            film = jarjend[0]
        kustutaFilm(film)
        print(tahis + " " + film + "\n" + "Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
while True:
    sisend = input("Sisesta käsklus:")
    tahis_zanr_film = sisend.split()
    tahis = tahis_zanr_film[0]    
    if tahis == "K":
        jarjend = [tahis_zanr_film [1]]
    elif tahis == "L":
        try:
            jarjend = [tahis_zanr_film [1]] + [tahis_zanr_film[2]] + [tahis_zanr_film[3]]
        except:
            jarjend = [tahis_zanr_film [1]] + [tahis_zanr_film[2]]
    elif tahis == "V":
        try:
            jarjend = [tahis_zanr_film[1]] + [tahis_zanr_film[2]]
        except:
            jarjend = [tahis_zanr_film[1]]
    if tahis == "E":
        break
    töötleKäsk(tahis, jarjend)