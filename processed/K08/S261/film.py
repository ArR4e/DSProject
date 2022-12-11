def loetleFilmid(zanr):
    filmid=[]
    for rida in read:
        rida=(rida.strip()).split(' - ')
        
        if zanr in rida:
            filmid+=[rida[0]]
    return filmid        
    
    
def lisaFilm(film,zanr):
    f=open('filmid.txt','a')
    f.write('\n'+film+' - '+zanr)
    f.close()
    
def kustutaFilm(film):
    filmid=[]
    for rida in read:
        rida=(rida.strip()).split(' - ')
        
        if film in rida:
            break
        else:
            filmid+=[' - '.join(rida)]
    f=open('filmid.txt','w')
    
    f.write('\n'.join(filmid))

    f.close() 
    
    
f=open('filmid.txt')
read=f.readlines()

f.close()


