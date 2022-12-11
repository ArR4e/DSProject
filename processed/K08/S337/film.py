def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    filmid = []
    for rida in f:
        rida = rida.split(' - ')
        if rida[1].strip() == žanr:
            filmid.append(rida[0].lstrip())
    f.close()
    return filmid
def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding='UTF-8')
    f.write(f'\n {nimi} - {žanr}')
    f.close()
def kustutaFilm(film):
    f = open('filmid.txt', 'r', encoding = 'UTF-8')
    read = f.readlines()
    uus = []
    for el in read:
        el = el.split(' - ')
        if el[0].lstrip() != film:
            el = ' - '.join(el)
            uus += el
    f.close()
    f = open('filmid.txt', 'w', encoding = 'UTF-8')
    f.write(''.join(uus))    
    f.close()