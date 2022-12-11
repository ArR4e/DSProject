def loetleFilmid(zanr):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()

    filmid = []
    filmid_ja_zanrid = []
    zanrid = []
    filmenimed = []

    for film in read:
        a = film.rstrip()
        filmid += [a]

    for i in filmid:
        jaotus = i.split(" - ")
        filmid_ja_zanrid += jaotus

    index = 0    
    for i in filmid_ja_zanrid:
        if index % 2 == 1:
            zanrid += [i]
        else:
            filmenimed += [i]
        index += 1
    vajadfilmid = []
    indeks = 0
    for i in zanrid:
        if i == zanr:
            vajadfilmid += [filmenimed[indeks]]
        indeks += 1
    return vajadfilmid

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()
    filmid = []
    filmid_ja_zanrid = []
    zanrid = []
    filmenimed = []

    for film in read:
        a = film.rstrip()
        filmid += [a]

    for i in filmid:
        jaotus = i.split(" - ")
        filmid_ja_zanrid += jaotus

    index = 0    
    for i in filmid_ja_zanrid:
        if index % 2 == 1:
            zanrid += [i]
        else:
            filmenimed += [i]
        index += 1
    f2 = open("filmid.txt", "w")
    for i in filmid:
        f2.write(i + "\n")
    f2.write(nimi + " - " + zanr + "\n")
    f2.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()

    filmid = []
    filmid_ja_zanrid = []
    zanrid = []
    filmenimed = []

    for film in read:
        a = film.rstrip()
        filmid += [a]

    for i in filmid:
        jaotus = i.split(" - ")
        filmid_ja_zanrid += jaotus

    index = 0    
    for i in filmid_ja_zanrid:
        if index % 2 == 1:
            zanrid += [i]
        else:
            filmenimed += [i]
        index += 1
    kolmas_index = 0
    for i in filmenimed:
        if nimi == i:
            del read[kolmas_index]
        kolmas_index += 1
    f4 = open("filmid.txt", "w")
    for i in read:
        f4.write(i)
    f4.close()
