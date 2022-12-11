def loetleFilmid(zanr):
    f=open("filmid.txt","r")
    sisu=f.read().split("\n")
    f.close()
    filmid=[]
    for rida in sisu:
        if rida=="":
            continue
        film=rida.split(" - ")
        z=film[1]
        if z==zanr:
            filmid.append(film[0])
    return filmid
    
def lisaFilm(nimi,z):
    f=open("filmid.txt","a")
    f.write("\n"+nimi+" - "+z)
    f.close()

def kustutaFilm(nimi):
    f=open("filmid.txt","r")
    sisu=f.read().split("\n")
    filmid=[]
    for rida in sisu:
        if nimi not in rida:
            filmid+=[rida]
    f.close()
    f=open("filmid.txt","w").close
    f=open("filmid.txt","w")
    f.write("\n".join(filmid))
    f.close()