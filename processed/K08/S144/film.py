def loetleFilmid(zanr):
    f = open('filmid.txt', 'r', encoding='utf-8')
    filmid = []
    while True:
        rida = f.readline()
        try:
            ajutine = rida[rida.index(' - ') + 3:].strip()
        except:
            break
        if ajutine == zanr:
            filmid += rida[:rida.index(' - ')].split('*')
    f.close()
    return filmid
def lisaFilm(nimi, zanr):
    f = open('filmid.txt', 'a', encoding='utf-8')
    f.write('\n' + nimi + ' - ' + zanr)
    f.close
def kustutaFilm(nimi):
    with open('filmid.txt', 'r', encoding='utf-8') as f:
        tekst = f.readlines()
    f = open('filmid.txt', 'w', encoding='utf-8')
    for i in tekst:
        if nimi not in i.strip():
            f.write(i)
    f.close()

