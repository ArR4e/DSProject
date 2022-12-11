def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = 'UTF-8')
    rida = f.readline
    filmid = []
    for rida in f:
        film = rida.strip().split(" - ")
        if žanr == film[-1]:
            filmid += film[0:1]
    return filmid
    f.close()
        
    
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = 'UTF-8')
    f.write("\n" + nimi + " - " + žanr)
    f.close()
    
def kustutaFilm(nimi):
    with open("filmid.txt", encoding = 'UTF-8') as f:
        read = f.readlines()
    with open("filmid.txt", "w", encoding = 'UTF-8') as f:
        for rida in read:
            if rida.strip().split(" - ")[0] != nimi:
                f.write(rida)