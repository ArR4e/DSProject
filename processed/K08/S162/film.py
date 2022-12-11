def loetleFilmid(zanr):
    f=open('filmid.txt')
    filmid=[]
    for rida in f:
        rida=rida.strip('\n')
        rida=rida.split(' - ')
        if rida[-1]==zanr:
            filmid.append(rida[0])
    f.close()
    return filmid
def lisaFilm(nimi,zanr):
    f=open('filmid.txt','a')
    f.write('\n'+nimi+' - '+zanr)
    f.close()
def kustutaFilm(nimi):
    f=open('filmid.txt')
    read=f.readlines()
    f.close()
    f=open('filmid.txt','w')
    for x in read:
        a=x.split(' - ')
        if a[0]!=nimi:
            f.write(read[read.index(x)])
    f.close()