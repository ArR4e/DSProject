def loetleFilmid(žanr):
    f = open("filmid.txt")
    filmid = []
    for rida in f:
        rida=rida.strip()
        if rida.endswith(žanr):
            rida = rida.split(' - ')
            x = [rida[0].strip()]
            filmid += x
    f.close()
    return filmid
def lisaFilm(nimi,žanr):
    f=open('filmid.txt','a')
    f.write('\n' + nimi + ' - ' + žanr)
    f.close()
def kustutaFilm(nimi):
    f = open('filmid.txt','r')
    filmid=f.readlines()
    f = open('filmid.txt','w')
    for rida in filmid:
        if not rida.startswith(nimi):
            f.write(rida)
    f.close()
