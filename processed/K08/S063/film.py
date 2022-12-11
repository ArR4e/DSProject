def loetleFilmid(žanr):
    filmid = []
    
    f = open('filmid.txt', 'r', encoding = 'utf-8')
    for rida in f:
        rida = rida.strip().split(' - ')
        if rida[0] != '':
            if rida[1] == žanr:
                filmid.append(rida[0])
    f.close()
    
    return filmid

def lisaFilm(nimi, žanr):
    lisa_film = ' - '.join([nimi, žanr])
    
    f = open('filmid.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    
    f = open('filmid.txt', 'a', encoding = 'utf-8')
    if not text.endswith('\n'):
        f.write('\n')
    if lisa_film not in text:
        f.write(lisa_film)
        return True
    else:
        return False
    f.close()

def kustutaFilm(nimi):
    film_leidub = False
    
    f = open('filmid.txt', encoding = 'utf-8')
    read = f.readlines()
    f.close()
    
    for rida in read:
        if rida.strip().split(' - ')[0] == nimi:
            film_leidub = True
    
    if film_leidub:
        f = open('filmid.txt', 'w', encoding = 'utf-8')
        for rida in read:
            if rida.strip().split(' - ')[0] != nimi:
                f.write(rida)
        f.close()
        return True
    else:
        return False
