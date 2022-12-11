def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    multikas = []
    märul = []
    õudukas = []
    for filmid in f:
        filmid = filmid.strip().split(' - ')
        for film in filmid:
            if film == 'multikas':
                multikas += [filmid[0]]
            elif film == 'märul':
                märul += [filmid[0]]
            elif film == 'õudukas':
                õudukas += [filmid[0]]
    if žanr == 'multikas':
        return multikas
    elif žanr == 'märul':
        return märul
    elif žanr == 'õudukas':
        return õudukas
    f.close()

def lisaFilm(nimi, žanr):
    f = open('filmid.txt','a', encoding = 'UTF-8')
    filmi_lisamine = f.write(str(nimi) + ' - ' + str(žanr) + '\n')
    f.close()
    return filmi_lisamine

def kustutaFilm(nimi):
    f = open('filmid.txt', encoding = 'UTF-8')