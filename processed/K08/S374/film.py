def loetleFilmid(zanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    read= f.readlines()
    f.close()
    
    filmid = []
    for rida in read:
        rida = rida.strip('\n')
 
        if rida.endswith(zanr):
            film = rida.split(' - ')
            filmid.append(film[0])
    
    return filmid


def lisaFilm(nimi, zanr):
    f = open('filmid.txt', 'a', encoding = 'UTF-8')
    f.write('\n')
    f.write(nimi+' - '+zanr)
    f.close()
  
def kustutaFilm(nimi):
    f1 = open('filmid.txt', encoding = 'UTF-8')
    read = f1.readlines()
    f1.close()
    
    index = 0
    for rida in read:
        film = rida.split(' - ')
        if film[0] == nimi:
            index = read.index(rida)
            break
        
    read.pop(index)
    
    f2= open('filmid.txt', 'w', encoding = 'UTF-8')
    
    for rida in read:
        f2.write(rida)
    f2.close()

        