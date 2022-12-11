def loetleFilmid(zanr):
    with open("filmid.txt", encoding="utf-8") as f:
        read = f.read().splitlines()
    f.close()
    filmid = []
    for x in read:
        kate_g = x.split(" - ", 1)[1]
        if kate_g == zanr:
            filmid.append(x.rpartition(' - ')[0])
    return filmid

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="utf-8")
    f.write("\n"+str(nimi)+" - "+str(zanr))
    f.close()
    

def kustutaFilm(filminimi):
    with open("filmid.txt",'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open("filmid.txt",'w', encoding="utf-8") as f:
        for line in lines:
        # find() returns -1 if no match is found
            if line.find(filminimi) != -1:
                pass
            else:
                f.write(line)
    
##lisaFilm('Borat', 'komöödia')
##lisaFilm('Ratatouille', 'multikas')
#####print(*loetleFilmid('multikas'), sep = "\n")