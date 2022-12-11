def loetleFilmid(žanr):
    f=open("filmid.txt", encoding="UTF-8")
    filmid=[]
    for rida in f:
        film=rida.strip().split(" - ")
        while film==[""]:
            film=f.readline().strip().split(" - ")          
        if film[1]==žanr:
            filmid=filmid+[film[0]]
            
    f.close()
    
    return filmid

def lisaFilm(nimi,žanr):
    f=open("filmid.txt", "r+", encoding="UTF-8")
    f.read()
    f.write("\n"+nimi+" - "+žanr)
    f.close()
        
def kustutaFilm(nimi):
    f=open("filmid.txt", "r", encoding="UTF-8")
    read=f.readlines() #https://www.kite.com/python/answers/how-to-delete-a-line-from-a-file-in-python
    f.close()
    f=open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if rida.strip().split(" - ")[0]!=nimi:
            f.write(rida)
    
    f.close()
    

    

    

    

