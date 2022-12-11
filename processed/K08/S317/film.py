def loetleFilmid(žanr):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    järjend = []
    while True:
        rida = fail.readline().strip()
        if rida == "":
            break
        filmjazanr = rida.split(" - ")
        if filmjazanr[1] == žanr:
            a = filmjazanr[0]
            järjend.append(a)
    fail.close()
    return järjend
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding="UTF-8")
    rida = nimi + " - " + žanr
    fail.write("\n")
    fail.write(rida)
    fail.close()
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    read = fail.readlines()
    fail.close()
    fail = open("filmid.txt", "w", encoding="UTF-8")
    for i in read:
        uus = i.strip("\n")
        järgmine = uus.split(" - ")
        õige = järgmine[0]
        if õige != nimi:
            fail.write(uus)
            fail.write("\n")
    fail.close()