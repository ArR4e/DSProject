import film
def töötleKäsk(tähis, järjend1):
    if tähis == "K":
        žanr = järjend1
        print("Võimalikud filmid on:")
        filmid = film.loetleFilmid(žanr)
        print("\n".join(filmid))
        if "\n".join(filmid) == "":
            print("Sellest žanrist pole ühtegi filmi, tee uus valik.")
    elif tähis == "L":
        järjend2 = järjend1.split()
        nimi2 = järjend2[0]
        žanr2 = järjend2[-1]
        film.lisaFilm(nimi2, žanr2)
        print("Film lisatud!")
    elif tähis == "V":
        nimi3 = järjend1
        film.kustutaFilm(nimi3)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    elif tähis == "E":
        return False
käsklus = input("Sisesta käsklus:")
käsklus1 = käsklus.split(" ")
tähis = käsklus1[0]
listipikkus = len(käsklus1)
järjend = käsklus1[1:listipikkus+1]
järjend1 = " ".join(järjend)
töötleKäsk(tähis, järjend1)

        
        