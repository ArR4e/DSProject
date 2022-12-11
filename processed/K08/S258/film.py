def openreader():
    f = open("filmid.txt","r")
    filmid1 = f.readlines()
    filmid=[]
    for x in filmid1:
        filmid.append([x.split("-")[0].strip(),x.split("-")[1].strip()])
    f.close()
    return filmid
def openwriter(outer):
    f = open("filmid.txt","w")
    for x in outer:
        f.write(str(x[0]+" - "+x[1]+"\n"))
    f.close()
def loetleFilmid(genre):
    filmid = openreader()
    esitada=[]
    for x in filmid:
        if x[1] == genre:
            esitada.append(x[0])
    return esitada
def lisaFilm(nimi,genre):
    algfilm=openreader()
    algfilm.append([nimi,genre])
    openwriter(algfilm)
def kustutaFilm(nimi):
    algfilm=openreader()
    for x in algfilm:
        if x[0]==nimi:
            algfilm.remove(x)
    openwriter(algfilm)