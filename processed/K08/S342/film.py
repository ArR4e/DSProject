def loetleFilmid(žanr):
    file = open("filmid.txt", encoding = "utf-8")
    filesisu = file.readlines()
    filmid = []
    for rida in filesisu:
        #print(rida)
        sõne = rida.strip().split(" - ")
        filminimi = sõne[0]
        #print(filminimi)
        žanrinimi = sõne[1]
        if žanrinimi == žanr:
            filmid.append(filminimi)
    return filmid
    #print(filmid)
    file.close()
def lisaFilm(a, b):
    file = open("filmid.txt", "a", encoding = "utf-8")
    filminimi = a
    žanrinimi = b
    file.write("\n" + a + " - " + b)
    #filesisu = file.readlines()
    #print(filesisu)
    file.close()
def kustutaFilm(nimi):
    file = open("filmid.txt", "r", encoding = "utf-8")
    filesisu = file.readlines()
    file.close()
    file2 = open("filmid.txt", "w", encoding = "utf-8")
    for rida in filesisu:
        if nimi not in rida:
            file2.write(rida)
    file2.close()