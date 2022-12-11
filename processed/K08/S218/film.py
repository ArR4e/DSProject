def loetleFilmid(žanr):
    filmi_järjend = []
    f = open("filmid.txt", "r", encoding="utf-8")
    for rida in f:
        ilma_reavahetuseta = rida.strip()
        osad = ilma_reavahetuseta.split(" - ")
        rea_järjend = list(osad)
        if rea_järjend[-1] == žanr:
            filmi_järjend.append(rea_järjend[0])
    f.close()
    return filmi_järjend

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "utf-8")
    f.write("\n")
    f.write(nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding="utf-8")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding="utf-8")
    for element in read:
        ilma_reavahetuseta = element.strip("\n")
        osad = ilma_reavahetuseta.split(" - ")
        rea_järjend = list(osad)
        if rea_järjend[0] != nimi:
            f.write(element)
    f.close()
