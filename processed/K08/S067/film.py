def loetleFilmid(žanr):
    try:
        f = open('filmid.txt', 'r+', encoding = 'UTF-8')
        sisu = f.read().strip().split('\n')
        nimed = []
        olemas = []
        for film in sisu:
            nimed.append(film.split(' - '))
        for x in nimed:
            if x[1] == žanr:
                olemas.append(x[0])
        f.close()
        return olemas
    except:
        return []
def lisaFilm(nimi, žanr):
    try:
        f = open('filmid.txt', 'r+', encoding = 'UTF-8')
        sisu = f.read().strip().split('\n')
        a = [str(nimi), ' - ', str(žanr)]
        f.write('\n')
        for i in a:
            f.write(i)
        f.close()
    except:
        return []
def kustutaFilm(nimi):
    try:
        f = open('filmid.txt', 'r+', encoding = 'UTF-8')
        sisu = f.read().strip().split('\n')
        i = 0
        nimed = []
        for film in sisu:
            nimed.append(film.split(' - '))
        f.seek(0)
        f.truncate(0)
        for x in nimed:
            if x[0] != nimi:
                f.write(sisu[i])
                f.write('\n')
                i += 1
            else:
                i += 1
        f.close()
    except:
        return []