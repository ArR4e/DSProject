#alustasin 15.10.2021 (22:30)
def loetleFilmid(zanr):
    f = open('filmid.txt', encoding = 'utf8')
    filmid = []
    for rida in f:
        info = rida.split(' - ')
        if info[-1] != '\n': #kui seda ei ole, siis tekkib viga mis on seotud funktsiooniga kustutaFilm()
            if zanr == info[-1].strip():
                filmid.append(info[0])
    f.close()
    return filmid

def lisaFilm(nimi, zanr):
    f = open('filmid.txt', 'a', encoding = 'utf8')
    uus_film = nimi + ' - ' + zanr
    f.write('\n' + uus_film)
    f.close()

def kustutaFilm(nimi):
    f = open('filmid.txt', 'r', encoding = 'utf8')
    read = f.readlines()
    f.close()
    f = open('filmid.txt', 'w', encoding = 'utf8')
    for rida in read:
        uus_rida = rida.split(' - ')
        if uus_rida[0].strip('\n') != nimi:
            f.write(rida)
    f.close()