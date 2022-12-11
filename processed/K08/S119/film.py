import os
def loetleFilmid(zanr):
    f = open("filmid.txt")
    read = f.readlines()
    f.close()
    films = []
    zanrid = []
    c = []
    justfilm = []
    index = 0
    for rida in read:
        rida = rida.strip()
        c = c + [rida]
        read = rida.split(" - ")
        justfilm = justfilm + read
    for el in justfilm:
        if index % 2 == 0:
            films = films + [el]
        else:
            zanrid = zanrid + [el]
        index = index + 1
    filmid = []
    i = 0
    for zan in zanrid:
        if zan == zanr:
            filmid = filmid + [films[i]]
        i += 1
    return filmid
def lisaFilm(nimi, zanr):
    f = open("filmid.txt")
    read = f.readlines()
    f.close()
    films = []
    zanrid = []
    c = []
    justfilm = []
    index = 0
    for rida in read:
        rida = rida.strip()
        c = c + [rida]
        read = rida.split(" - ")
        justfilm = justfilm + read
    for el in justfilm:
        if index % 2 == 0:
            films = films + [el]
        else:
            zanrid = zanrid + [el]
    index = index + 1
    a = open("filmid.txt", "w")
    for i in c:
        a.write(i + "\n")
    a.write(nimi + " - " + zanr + "\n")
    a.close()

def kustutaFilm(nimi):
    f = open("filmid.txt")
    read = f.readlines()
    f.close()
    films = []
    zanrid = []
    c = []
    justfilm = []
    index = 0
    for rida in read:
        rida = rida.strip()
        c = c + [rida]
        read = rida.split(" - ")
        justfilm = justfilm + read
    for el in justfilm:
        if index % 2 == 0:
            films = films + [el]
        else:
            zanrid = zanrid + [el]
        index = index + 1
    d = 0
    for film in films:
        if nimi == film:
            del c[d]
        d += 1
    b = open("filmid.txt", "w")
    for l in c:
        b.write(l + "\n")
    b.close()
        
            
kustutaFilm("Shrek")


