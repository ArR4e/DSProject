import film

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        print(film.loetleFilmid(järjend))
        return True
    elif käsk == "L":
        splitter = järjend.index(" ")
        film.lisaFilm(järjend[splitter + 1:], järjend[: splitter])
        return True
    elif käsk == "V":
        film.kustutaFilm(järjend)
        return True
    elif käsk == "E":
        return False


while True:
    käsk = input()
    if töötleKäsk(käsk[0], käsk[2:]) == False:
        break
    