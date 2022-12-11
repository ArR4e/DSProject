from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(käsk, järjend):
    if käsk == K:
        print('Võimalikud filmid on: ')
        print(järjend)
        return True
    elif käsk == "L":
        lisaFilm(žanr, nimi)
        return True
    elif käsk == "V":
        kustutaFilm(nimi)
        return True
    elif käsk == "E":
        return False

Käsud = ["K", "L", "V", "E"]
töötleKäsk(K, märul)