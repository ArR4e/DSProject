def loetleFilmid(zanr):
    f=open("filmid.txt")
    tüüp=zanr+"\n"
    filmid=[]
    tüübid=[]
    for rida in f:
        osad=rida.split(" - ")
        zanrid=osad[1]
        if zanrid==tüüp:
            filmid=filmid+[osad[0]]
    print(filmid)

    f.close()
loetleFilmid("õudukas")


def lisaFilm(nimi,zanr):
    f2=open("filmid.txt", "a")
    f2.write("\n"+nimi+" - "+zanr)
    f2.close()

lisaFilm("Üksinda kodus","komöödia")

def kustutaFilm(nimi):
    with open("filmid.txt", "r") as f3:
        loe=f3.readlines()
    muuvi=nimi
    with open("filmid.txt", "w") as f3:
        for line in loe:
            if line.find(muuvi) != -1:
                pass
            else:
                f3.write(line)
    f3.close()
kustutaFilm("Moana")