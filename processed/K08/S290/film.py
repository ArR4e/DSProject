def loetleFilmid(žanr):
    f = open("filmid.txt")
    filmid = []
    for rida in f:
        rida = rida.split(" - ")
        žanr2 = rida[1]
        if žanr == str.rstrip(žanr2):
            filmid += [rida[0]]
    return filmid
    f.close()

def lisaFilm(nimi, žanr):
    f = open("filmid.txt")
    f.write(str(nimi) + " - " + str(žanr))
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt")
    for rida in f:
        nimi2 = rida[0]
        if nimi != str.rstrip(nimi2):
            f.write(rida)
    f.close()
        


        
