def loetleFilmid(zanr):
    f = open('filmid.txt', 'r', encoding='utf-8')
    järjend = []
    for el in f:
        rida = el.rstrip()
        if rida.endswith(zanr):
            a = rida.strip(zanr)
            b = a.strip(' -')
            järjend.append(b)
    f.close()
    return järjend
    
def lisaFilm(nimi, zanr):
    f = open('filmid.txt', 'a', encoding='utf-8')
    f.write('\n' + nimi + ' - ' + zanr)
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt', 'r', encoding='utf-8')
    read = f.readlines()
    f.close()
    f1 = open('filmid.txt', 'w', encoding='utf-8')
    for rida in read:
        if not rida.startswith(nimi):
            f1.write(rida)
    f1.close()