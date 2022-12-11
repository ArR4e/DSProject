
f = open("filmid.txt", encoding = "UTF-8")

read = f.readlines()

    
def loetleFilmid(žanr):    
    filmilist = []
    for rida in read:
        rida = rida.strip().split(" - ")
        žanr1 = rida[-1]
        film = rida[0]
        if žanr1 == žanr:
            filmilist.append(film)
    return filmilist

f.close()

f = open("filmid.txt", "a", encoding = "UTF-8")

def lisaFilm(nimi, žanr):
    nimi = f.write(str(nimi) + " - ")
    žanr = f.write(žanr)
    return nimi + žanr
    
f.close()


def kustutaFilm(film):
    with open("filmid.txt") as f:
        read = f.readlines()
    with open("filmid.txt", "w") as f:
        for rida in read:
            film1 = rida.strip("\n").split(" - ")[0]
            if film1 != film:
                f.write(rida)
                
f.close()
        
            
        