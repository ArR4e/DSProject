import film
def töötleKäsk(tah, jarj):
    if tah == 'K':
        film.loetleFilmid(jarj)
    elif tah == 'L':
        jarj = jarj.split(' ', -1)
        film.lisaFilm(jarj[0], jarj[1])
    elif tah == 'V':
        film.kustutaFilm(jarj)
    elif tah == 'E':
        return False
while True:   

    inp = input("Sisesta, mida teha soovid: ")
    m = inp.split(' ', 1)

    töötleKäsk(m[0], m[1])

