
def loetleFilmid(tüüp):
    f = open("filmid.txt", "r+", encoding="utf8")
    järjend = []
    for rida in f: #leiab kõik filmid ja zanrid
        
        sisu = rida.split(" - ")
        film = sisu[0].strip()
        zanr = sisu[1].strip()
        if zanr == tüüp:
            järjend.append(film)
    f.close()
    return järjend

def lisaFilm(nimi, tüüp):
    f = open("filmid.txt", "r+", encoding="utf8")
    f.seek(0, 2)
    f.write("\n " + nimi + " - " + tüüp)
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt", "r+", encoding="utf8")
    faili_sisu = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding="utf8")
    i=0
    for rida in faili_sisu:
        i += 1
        if nimi not in rida:
            if i == 1:
                f.write(rida.strip("\n"))
            else:
                f.write("\n")
                f.write(rida.strip("\n"))
    f.close()