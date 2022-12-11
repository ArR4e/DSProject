import os

def loetleFilmid(teema):
    
    f = open("filmid.txt", encoding="utf-8")

    filmid = []

    for rida in f:
        rida = rida.strip().rsplit("-", 1)
        filmid.append(rida)
    
    valik = []
    
    for genre in filmid:
        if str(genre[1]).strip() == teema:
            valik.append(str(genre[0]).strip())
    
    return valik
    
    f.close()

def lisaFilm(nimi, teema):
    
    f = open("filmid.txt", "a", encoding="utf-8")
    
    if os.stat('filmid.txt').st_size == 0:
        f.write(str(nimi)+" - "+str(teema))
    else:
        f.write("\n"+str(nimi)+" - "+str(teema))
  
    f.close()

def kustutaFilm(teema):
    
    f = open("filmid.txt", "r",encoding="utf-8")
    lines = f.readlines()
    f.close()
    
    f = open("filmid.txt", "w", encoding="utf-8")
    for line in lines:
        line = line.strip().rsplit("-", 1)
        if str(line[0]).strip() != teema:
            f.write(str(line[0]).strip()+" - "+ str(line[1]).strip()+"\n")
        
    f.close()