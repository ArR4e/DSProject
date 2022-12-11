def loetleFilmid(žanr):
    f = open('filmid.txt', 'r', encoding = 'latin1')
    filminimed = []
    for rida in f:
        if žanr in rida:
            rida = rida.strip()
            rida = rida.split(' - ')
            filminimed.append(rida[0])
        else:
            continue
    f.close()    
    return filminimed

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'latin1')
    film = "\n" + nimi + " - " + žanr
    f.write(film)
    f.close()  

def kustutaFilm(nimi):
    f = open('filmid.txt', 'r+', encoding = 'latin1')
    read = f.readlines()
    filmid = []
    for film in read:    
        if nimi not in film:
            filmid.append(film)
    f.close()
    f = open('filmid.txt', 'w', encoding = 'latin1')
    for i in range(0, len(filmid)):
        f.write(filmid[i])
    f.close()  