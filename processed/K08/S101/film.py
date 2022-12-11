


def loetleFilmid(n):
    f=open("filmid.txt")
    filmid=[]
    for e in f:
        e=e.strip()
        film=e.split("-")
        if len(film)>2:
            film=["-".join(film[0:(len(film)-1)]),film[len(film)-1]]
        if film[len(film)-1]==" "+n:
            film=[film[0].strip()]
            filmid=filmid+film
    f.close()
    return(filmid)

def lisaFilm(nimi,žanr):
    f=open("filmid.txt","a")
    film=" - ".join([nimi,žanr])
    f.write("\n"+film)
    f.close()
    
    
def kustutaFilm(nimi):
    f=open("filmid.txt")
    read=f.readlines()
    f.close()
    f=open("filmid.txt")
    n=-1
    for e in f:
        n+=1
        film = e.split("-")
        if len(film)>2:
            film=["-".join(film[0:(len(film)-1)]),film[len(film)-1]]
        if film[0].strip(" ")==nimi:
            del read[n]
    f.close()
    f=open("filmid.txt","w")
    n=0
    for i in read:
        f.write(read[n])
        n+=1

