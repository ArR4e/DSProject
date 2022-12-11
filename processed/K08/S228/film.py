def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    filmid = []
    for rida in f:
        rida_ok = rida.strip().split(' - ')
        if rida_ok[-1] == žanr:
            filmid.append(rida_ok[0])
    f.close()
    return filmid

#print(loetleFilmid('multikas')), katsetamiseks

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'UTF-8')
    tekst = '\n' + nimi + ' - ' + žanr
    f.write(tekst)
    f.close
    
#lisaFilm('Shrek2', 'multikas'), katsetamiseks

def kustutaFilm(nimi):
    f = open('filmid.txt', 'rt', encoding = 'UTF-8')
    filmid = f.readlines()
    print(filmid)
    f.close()
    f = open('filmid.txt', 'w+', encoding = 'UTF-8')
    uus_sisu = ''
    for film in filmid:
        film_ok = film.strip().split(' - ')
        if film_ok[0] != nimi:
            uus_sisu += film
    f.write(uus_sisu)
    f.close()
            
#kustutaFilm('Shrek2'), katsetamiseks