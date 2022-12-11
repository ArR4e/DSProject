def loetleFilmid(a):
    if a != '':
        fail = open('filmid.txt', encoding = 'UTF-8')
        filmid = []
        for rida in fail:
            if a in rida:
                rida = rida.split(' - ')
                filmid.append(rida[0])
        fail.close()
        return(filmid)
    else:
        return('')

def lisaFilm(a,b):
    fail = open('filmid.txt', 'a' ,encoding = 'UTF-8')
    a = a.capitalize()
    b = b.lower()
    film = (a + ' - ' + b)
    fail.write('\n'+film )
    fail.close()
    return(film)
    
def kustutaFilm(a):
    read = []
    t = False
    fail = open('filmid.txt', encoding = 'UTF-8')
    read = fail.readlines()
    fail = open('filmid.txt', 'w' , encoding='UTF-8')
    a = a.capitalize()
    for rida in read:
        if a in rida:
            t = True
        else:
            fail.write(rida)
    fail.close()
    return t