import re

f = open("filmid.txt", "r", encoding="UTF-8")
filmid = []
for i in f :
    zanr = i.split("-")[1].strip()
    nimi = i.split("-")[0].strip()
    filmid.append(zanr)
    filmid.append(nimi)
  
f.close()
#print(filmid)
def loetleFilmid(zanr):
    listid = []
    loetle = filmid
    mitu = filmid.count(zanr)
    for i in range(mitu):
        if zanr in loetle:
            indeks = loetle.index(zanr)
            listid.append(loetle[indeks + 1])
            loetle.pop(indeks)
    return listid

def lisaFilm(nimi : str, zanr : str):
    f= open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n"+ nimi + " - "+ zanr + "\n")
    f.close()

def kustutaFilm(nimi_kustuta):
    f = open("filmid.txt", "r+", encoding="UTF-8")
    for i in f:
        if i.split("-")[0].strip() != nimi_kustuta:
            f.write(i)
            continue
        else :
            continue
    f.close()


lisaFilm("Viikingid", "ajalooline")



