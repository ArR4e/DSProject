def loetleFilmid(zanr_antud):
    f=open("filmid.txt", encoding="UTF-8")
    i=0
    filmid = []
    for rida in f:
        sisu = rida.split(" - ")
        zanr = sisu[-1]
        zanr = zanr.replace("\n","")
        if zanr_antud == zanr:
            film = sisu[0]
            filmid = filmid + [film]
            i+=1
        else:
            i+=1
    f.close()
    return(filmid)  

def lisaFilm(film_uus,zanr_uus):
    uus = film_uus + " - " + zanr_uus
    with open("filmid.txt", "r+", encoding="UTF-8") as f:
        f.read()
        f.write("\n")
        f.write(uus)

def kustutaFilm(kustuta_film):
    with open("filmid.txt","r") as f:
        read = f.readlines()
    with open ("filmid.txt","w") as f:
        for rida in read:
            if kustuta_film not in rida:
                f.write(rida)
