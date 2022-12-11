def loetleFilmid(sanr):
    f=open("filmid.txt","r",encoding="utf-8")
    l=[]
    for line in f:
        if sanr in line.split(" - ")[1]:
            l.append(line.split(" - ")[0])
    f.close()
    return l
def lisaFilm(nimi,sanr):
    f=open("filmid.txt","a",encoding="utf-8")
    film=("\n"+nimi+" - "+sanr)
    f.write(film)
    f.close()
def kustutaFilm(film):
    f=open("filmid.txt","r",encoding="utf-8")
    t=f.readlines()
    f.close()
    f=open("filmid.txt","w",encoding="utf-8")
    for el in t:
        if film not in el:
            f.write(el)        
    f.close()