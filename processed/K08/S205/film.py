
def loetleFilmid(žanr):
    filmid = []
    with open('filmid.txt', 'r', encoding='UTF-8') as file:
        film=[]
        for rida in file:
            if žanr in rida:
                filmid.append(rida.split(' - ')[0])
            #film = rida.strip('\n')
            #film = film.strip(' ')
            #film = film.split('-')
            #read.append(film)
    return filmid

def lisaFilm(nimi, žanr):
    film = (nimi + ' - ' +žanr)
    tekst = []
    with open('filmid.txt', 'a+', encoding='UTF-8') as file:
        tekst = file.read()
        if not len(tekst):
            file.write('\n')
        file.write(film)
        
def kustutaFilm(nimi):
    filmid = []
    filmid_sõnena=''
    with open('filmid.txt', 'r+', encoding='UTF-8') as file:
        for rida in file:
            if not nimi in rida:
                filmid.append(rida)
        for el in filmid:
            filmid_sõnena += el
    with open('filmid.txt', 'w', encoding='UTF-8') as file:
        file.write(filmid_sõnena)