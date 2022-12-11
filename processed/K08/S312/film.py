def loetleFilmid(zanr):
    on = []
    f = open('filmid.txt')
    for rida in f:
        rida = rida.strip()
        ridalahti = rida.split(' - ') 
        if ridalahti[1] == zanr:
            on += [ridalahti[0]]
    f.close()        
    return(on)
    
        
def lisaFilm(nimi, zanr):
    f = open('filmid.txt', 'a')
    element = [nimi, zanr]
    elementkokku = ' - '.join(element)
    f.write('\n' + elementkokku + '\n')
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt', 'r')
    jarjend = f.readlines()
    f.close()
    kustutatud = open('filmid.txt', 'w')
    for el in jarjend:
        if nimi not in el.strip():
           kustutatud.write(el)
    kustutatud.close()
    
    
            