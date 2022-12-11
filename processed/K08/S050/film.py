

def loetleFilmid(zanrinimi):
    f=open('filmid.txt', 'r+', encoding='UTF-8')
    filmid=[]
    for rida in f:
        rida=rida.split(' - ')
        if rida[-1].strip() == zanrinimi:
            filmid.append(rida[0].lstrip())
    f.close()
    return filmid

  
def lisaFilm(nimi,zanr):
    f=open('filmid.txt', 'a', encoding='UTF-8')
    f.write('\n' +nimi+ ' - ' +zanr)
    f.close



def kustutaFilm(nimi):
    f=open('filmid.txt', 'r', encoding='UTF-8')
    nimekiri=f.readlines()
    for rida in nimekiri:
        if nimi in rida:
            nimekiri.remove(rida)
    f.close()
    f=open('filmid.txt', 'w', encoding='UTF-8')
    for film in nimekiri:
        f.writelines(film)
    f.close()
    