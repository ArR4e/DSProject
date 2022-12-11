def loetleFilmid(a):
    f=open("filmid.txt")
    filmid=[]
    b=[]
    for rida in f:
        filmid+=rida.strip().split(' - ')
    for film in filmid:
        if film==a:
            b.append(c)
        c=film
    f.close()
    return b

def lisaFilm(nimi, a):
    f=open('filmid.txt', 'a')
    f.write(f'\n {nimi} - {a} ')
    f.close()
    
def kustutaFilm(nimi):
    f=open('filmid.txt', 'r')
    b=''
    for rida in f:
        c=rida.strip().split(' - ')
        if c[0]!=nimi:    
            b+=rida
    f.close()
    f=open('filmid.txt', 'w')
    f.write(b)
    f.close()
    

    