#film
def loetleFilmid(žanr):
    f = open("filmid.txt")
    filmilist = []

    for rida in f:
        if žanr in rida:
            eemaldan_žanri = rida.strip().replace(žanr, "") #eemaldan reast žanri nimetuse
            film = eemaldan_žanri.replace(" - ", "") #eemaldan reast sidekriipsu ja tühiku
            filmilist.append(film)
    return filmilist
    f.close()
 
    

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a")
    film = nimi + " - " + žanr + "\n"
    f.write("\n"+film)
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w")
    for rida in read:
        if nimi not in rida:
            f.write(rida)
    f.close()
    
