import film

def töötleKäsk(k, j):
    if k == "K":
        print(film.loetleFilmid(j[0]))
        return True
    elif k == "L":
        film.lisaFilm(j[1], j[0])
        return True
    elif k == "V":
        film.kustutaFilm(j[1])
        return True
    else:
        return False

while True:
    sisend = str(input("Sisend: "))
    sisend = sisend.split()
    käsk = sisend[0]
    järjend = ["", ""]
    if käsk == "K":
        järjend[0] = sisend[1]
    elif käsk == "L":
        if len(sisend) > 3:
            i = 2
            nimi = ""
            while i < len(sisend):
                nimi = nimi + sisend[i]
                if i + 1 < len(sisend):
                    nimi += " "
                i += 1
        else:
            nimi = sisend[2]
        järjend[0] = sisend[1]
        järjend[1] = nimi
    elif käsk == "V":
        if len(sisend) > 2:
            i = 1
            nimi = ""
            while i < len(sisend):
                nimi = nimi + sisend[i]
                if i + 1 < len(sisend):
                    nimi += " "
                i += 1
            järjend[0] = sisend[1]
            järjend[1] = nimi
        else:
            nimi = sisend[1]
        järjend[1] = nimi
    else:
        break

    töötleKäsk(käsk, järjend)