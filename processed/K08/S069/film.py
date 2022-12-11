def loetleFilmid(nimi):
    nimi = str(nimi)
    fail = open('filmid.txt', 'r')
    järjend = []
    for line in fail:
        array = []
        for sõna in line.split():
            array += [sõna]
        array.remove("-")
        if nimi in array:
            array.remove(nimi)
            järjend += [''.join(array)]
    fail.close()
    return järjend
        

def lisaFilm(nimi, liik):
    fail = open('filmid.txt', 'a')
    lisa = str(nimi+' - '+liik)
    fail.write('\n')
    fail.write(lisa)
    
    fail.close()

def kustutaFilm(nimi):
    fail = open('filmid.txt', 'r')
    järjend = fail.readlines()
    fail.close()
    fail = open('filmid.txt', 'w')
    for line in järjend:
        delet = []
        for sõna in line.split():
            delet += [sõna]
        delet.remove("-")
        delet.reverse()
        delet.pop(0)
        delet.reverse()
        title = ' '.join(delet)           
        if title == nimi:
            a = 1
        else:
            a = 0
        if a == 0:
            fail.write(line)
    fail.close()
    

          


    
    
    
    
    