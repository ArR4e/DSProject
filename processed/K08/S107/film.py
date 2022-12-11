
def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "utf-8")
    #tühi järjend
    filmid = [] 
    for rida in f:
        #moodustab järjendi
        film = rida.strip().split(" - ")

        if film[1] == žanr: 
            filmid.append(film[0])
    f.close()       
    return filmid



def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "utf-8")
    f.write('\n')
    f.write(nimi)
    f.write(" - "+žanr + "\n")
    f.close()
  
def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding ="utf-8")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding = "utf-8")
    for rida in read:
        film = rida.strip().split(" - ")
            
        if film[0] != nimi:
            f.write(rida)
    f.close()
        