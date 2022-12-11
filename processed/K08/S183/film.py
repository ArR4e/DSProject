# I
def loetleFilmid(žanri_nimi):
    with open ("filmid.txt", encoding = "UTF-8") as film1:
        read = []
        for i in film1:
            žanr = i.strip("\n")
            žanr1 = žanr.split(" - ")
            if žanri_nimi in žanr1:
                read +=  [žanr1[0]]
    return read           

# II
def lisaFilm(fi_nimi, žanr_ni):
    with open ("filmid.txt", "a", encoding = "UTF-8") as film2:
        film2.write("\n" + fi_nimi + " - " + žanr_ni)

# III
def kustutaFilm(filmi_nimi):
    with open ("filmid.txt", "r", encoding = "UTF-8") as film3:
        read = film3.readlines()
        with open ("filmid.txt", "w", encoding = "UTF-8") as film4:
            for rida in read:
                žanr = rida.strip("\n")
                žanr1 = žanr.split(" - ")
                if filmi_nimi not in žanr1:
                    film4.write(rida)

    