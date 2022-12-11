def loetleFilmid(zanr):
    f = open('filmid.txt', encoding='utf-8')
    filmid = []
    for rida in f:
        hetke_rida = rida.strip().split(' - ')
        if hetke_rida == '':
            continue
        if hetke_rida[1] == zanr:
            filmid.append(hetke_rida[0])
    f.close()
    return filmid

def lisaFilm(uus_film, uus_zanr):
    f = open('filmid.txt', 'a', encoding='utf-8')
    f.write('\n')
    f.write(uus_film)
    f.write(' - ')
    f.write(uus_zanr)
    f.close()

def kustutaFilm(filmi_nimi):
    f = open('filmid.txt', 'r', encoding='utf-8')
    read = f.readlines()
    f.close()
    f = open('filmid.txt', 'w', encoding='utf-8')
    for rida in read:
        osad = rida.strip().split(' - ')
        nimed = osad[0]
        if nimed != filmi_nimi:
            f.write(rida)
    f.close()