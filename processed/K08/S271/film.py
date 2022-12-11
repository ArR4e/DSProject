def loetleFilmid(zanr):
    r = open('filmid.txt', 'r', encoding="UTF-8")
    filmid = []
    film = ''
    for rida in r:
        if rida.endswith(zanr) or rida.endswith(zanr+'\n'):
            film = (rida.replace(zanr, '').replace(' - ', '').replace('\n', ''))
            filmid.append(film)
    r.close()
    return filmid

def lisaFilm(nimi, zanr):
    a = open('filmid.txt', 'a', encoding="UTF-8")
    sisend =  '\n' + nimi + ' - ' + zanr
    a.write(sisend)
    a.close()

def kustutaFilm(nimi):
    r = open('filmid.txt', 'r', encoding="UTF-8")
    uus_sisu = ''
    for film in r:
        if film.startswith(nimi) == False:
            uus_sisu += film
    w = open('filmid.txt', 'w', encoding="UTF-8")
    w.write(uus_sisu)         