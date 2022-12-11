f = open("filmid.txt")
read = f.readlines()
f.close()

def loetleFilmid(žanri_nimi):
    filmid = []
    for i in range(len(read)):
        rida = (read[i].strip('\n')).split(' - ')
        if rida[1] == žanri_nimi:
            filmid = filmid + [rida[0]]
    return filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a")
    f.write('\n' + nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    with open("filmid.txt", "r") as file:
        filmid=file.readlines()
    with open("filmid.txt", "w") as file:
        for rida in filmid:
            rida1 = (rida.strip('\n')).split(' - ')
            if rida1[0] != nimi:
                file.write(rida)
