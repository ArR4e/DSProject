def baas():
    f = open('filmid.txt', 'r', encoding = 'utf-8')
    read = f.readlines()
    f.close()
    filmid = []
    
    for rida in read:
        filmid = filmid + [rida.strip()]
    return filmid
        
def loetleFilmid(žanr):
    filmid = baas()
    loetelu = []
    for film in filmid:
        if žanr in film:
            loetelu = loetelu + [film.split(' - ')[0]]
        else:
            continue
    return loetelu

def lisaFilm(nimi, žanr):
    filmid = baas()
    f2 = open('filmid.txt', 'w', encoding = 'utf-8')
    for rida in filmid:
        f2.write(rida + '\n')
    f2.write((nimi + ' - ' + žanr))
    f2.close()
    
def kustutaFilm(nimi):
    filmid = baas()
    f2 = open('filmid.txt', 'w', encoding = 'utf-8')
    for rida in filmid:
        if nimi not in rida:
            f2.write(rida + '\n')
    f2.close