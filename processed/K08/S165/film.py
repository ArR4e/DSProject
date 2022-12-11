def loetleFilmid(zanr):
    filmid = []
    f = open("filmid.txt","r",encoding = "latin-1")
    for film in f:
        if zanr in film:
            filmid.append(film.strip().split(" - ")[0])
    
    return filmid




def lisaFilm(nimi,zanr):
    f = open("filmid.txt","a")
    f.write("\n{0} - {1}".format(nimi,zanr))
    
    


def kustutaFilm(filminimi):
    f = open("filmid.txt","r")
    read = f.readlines()
    
    for film in read:
        if filminimi in film:
            read.remove(film)
            break
    read = "".join(read)
    f.close()
    f= open("filmid.txt","w")
    f.write(read)
    f.close()
    
    
           
    
    
    
    
  
    
    
    
    
    

