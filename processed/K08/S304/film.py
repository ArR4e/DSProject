def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    nimedelist = []
    
    for rida in f:
        rida = rida.split('-')
        nimi = rida[0]
        ž = rida[-1].strip()
        if ž == žanr:
            nimedelist.append(nimi)
            
    print(nimedelist)
        
    f.close()
            
           
def lisafilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'UTF-8')
    uus = '\n '+ nimi +'  -  '+ žanr
    
    f.writelines(uus)
    
    
    f.close() 

def kustutaFilm(nimi):
    f = open('filmid.txt', 'a+', encoding = 'UTF-8')

    for rida in f:
        rida = rida.split('-')
        nimiF = rida[0].strip()
        rida = ' '.join(map(str, rida))
        if nimiF == nimi:
            f.append(rida)
    
    f.close() 


# loetleFilmid("multikas")
#  lisafilm('Moana', 'multikas')
kustutaFilm('Shrek')