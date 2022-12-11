def loetleFilmid(nimi):
    
    f = open("filmid.txt")
    fail = f.readlines()
    
    nimed = []
    n = 0
    
    for i in fail:
        
        nimi1 = str(fail[n]).strip("\n")
        n += 1
        
        if nimi1.endswith(nimi):
            
            nimi1 = nimi1.replace(" - " + nimi, "")
            nimed = nimed + [nimi1]
    
    f.close()
    
    return(nimed)
            
def lisaFilm(nimi, zanr):
    
    f = open("filmid.txt", "a")
    f.write("\n" + nimi + " - " + zanr)
    f.close()
    
def kustutaFilm(nimi):
    
    f = open("filmid.txt", "r")
    fail = f.readlines()
    f.close()
    
    f1 = open("filmid.txt", "w")
    
    for line in fail:
        
        if line.startswith(nimi):
            
            f1.write("")
            
        else:
            
            f1.write(line)
            
    f1.close()