def loetleFilmid(a):
    filmid=open("filmid.txt","r",encoding="utf8")
    n=[]
    #filmide_järjend=filmid.strip()
    #filmide_järjend=filmide_järjend.split("\n")
    for film in filmid:
        film=film.strip()
        film=film.split(" - ")
        if film=="\n":
                filmid.close()
                return n
        elif film[1]==a:
            n+=[film[0]]
    filmid.close()
    return n

def lisaFilm(a, b):
    filmid=open("filmid.txt","a",encoding="utf8")
    e="\n" + str(a) + " - " + str(b)
    filmid.write(e)
    filmid.close()
    
def kustutaFilm(a):
    filmid=open("filmid.txt","r",encoding="utf8")
    n=[]
    for film in filmid:
        film=film.strip()
        film=film.split(" - ")
        if film[0]== a:
            continue
        else:
            n+=[" - ".join(film)]
    filmid.close()
    filmid=open("filmid.txt","w",encoding="utf8")
    filmid.write(" \n".join(n))
    filmid.close()