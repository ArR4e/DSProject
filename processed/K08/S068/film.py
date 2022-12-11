def loetleFilmid(a):
    film=[]
    f=open("filmid.txt",encoding="UTF-8")
    for rida in f:
        rida=rida.strip().split(" - ")
        if rida[1]==a:
            film.append(rida[0])
    f.close()
    return film 
    
def lisaFilm(a,b):
    f=open("filmid.txt", "a")
    f.write(a + " - " + b + "\n")
    f.close()

    
def kustutaFilm(a):
    f=open("filmid.txt","r")
    read=f.readlines()
    fuus=open("filmid.txt","w")
    for rida in read:
        if rida.strip().split(" - ")[0] != a:
            fuus.write(rida)
        
    fuus.close()
    
kustutaFilm("Avengers: End Game")