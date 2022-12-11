import film
def töötleKäsk(käsu_tähis, järjend):
    if käsu_tähis=="K":
        žanr=järjend[0]
        print(film.loetleFilmid(žanr))
    elif käsu_tähis=="L":
        filmi_nimi=järjend[1]
        žanr=järjend[0]
        film.lisaFilm(filmi_nimi, žanr)
        print("Film lisatud!")
    elif käsu_tähis=="V":
        filmi_nimi=" ".join(järjend)
        film.kustutaFilm(filmi_nimi)
        print("Film on nimekirjast kustutatud!")
    elif käsu_tähis=="E":
        return(True)
    else:
        return(False)


g=input("> ").split(" ")
while True:
    if g[0]=="E":
        break
    else:
        töötleKäsk(g[0], g[1:])
    g=input("> ").split(" ")   
        