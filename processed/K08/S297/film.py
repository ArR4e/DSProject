def loetleFilmid(zanr) :
    with open('filmid.txt', 'r', encoding='utf-8') as f:
        filmide_nimekiri = [el.splitlines() for el in f.readlines()]
        return filmide_nimekiri.pop()


def lisaFilmid(nimi, zanr) :
    with open('filmid.txt', 'a', encoding='utf-8') as f:
        lisatav_film = f'\n{nimi} - {zanr}'
        f.write(lisatav_film)
        
#def kustutaFilm(nimi) :
    #with open('filmid.txt', 'r+', encoding='utf-8') as f:
        
