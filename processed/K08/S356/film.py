def loetleFilmid(zanr):
    f = open("filmid.txt", encoding ="UTF-8")
    read = f.readlines()
    filmid = [i.replace("\n", "") for i in read]
    vastus = []
    for i in filmid:
        if zanr in i:
            vastus = vastus + [i]
            vastus = [i.replace(" - "+zanr, "") for i in vastus]
    
    return(vastus)
    
    f.close()
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding ="UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding ="UTF-8")
    lines = f.readlines()
    f = open("filmid.txt", "w", encoding ="UTF-8")
    for line in lines:
        if nimi not in line.strip("\n"):
            f.write(line)
    f.close()





