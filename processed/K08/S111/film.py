def loetleFilmid(zanr):
    fail=open("filmid.txt")
    filmid=[]
    for rida in fail:
        rida=rida.strip()
        rida=rida.split(" - ")
        if zanr in rida:
            filmid.append(rida[0])
    fail.close()
    return filmid
def lisaFilm(nimi, zanr):
    fail=open("filmid.txt", "a")
    fail.write("\n" + nimi + " - " + zanr)
    fail.close()
def kustutaFilm(nimi):
    fail=open("filmid.txt")
    read=fail.readlines()
    fail.close()
    fail2=open("filmid.txt", "w")
    for rida in read:
        rida=rida.strip()
        rida=rida.split(" - ")
        if rida[0]!= nimi:
            fail2.write(str(rida[0] + " - " + rida[1] + "\n"))
    fail2.close()
