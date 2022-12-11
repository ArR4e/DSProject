from film import loetleFilmid, lisaFilm, kustutaFilm


def töötleKäsk(tähis, järjend):
    if tähis == "K":
        žanr = järjend
        filmid = loetleFilmid(str(žanr))
        print("Võimalikud filmid on:")
        for film in filmid:
            print(str(film))
        return True
    
    elif tähis == "L":
        žanr = järjend.split(" ", 1)[0]
        film = järjend.split(" ", 1)[1]
        lisaFilm(str(film), str(žanr))
        print("Film lisatud!")
        return True
    
    elif tähis == "V":
        film = järjend
        kustutaFilm(str(film))
        print("Head vaatamist!")
        return True
    elif tähis == "E":
        return False

print("=== FILMIADMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta       E\n===")
while True:
    sisestus = input("")
    if sisestus == "E":
        tähis = sisestus
        break
    else:
        tähis = sisestus.split(" ", 1)[0]
        järjend = sisestus.split(" ", 1)[1]
        töötleKäsk(tähis, järjend)



