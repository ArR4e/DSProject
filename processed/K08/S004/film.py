def loetleFilmid(zanr):
    finallist=[]
    with open("filmid.txt","r",encoding="utf-8") as f:
        tekst=f.read().splitlines()
        f.close()
    for x in tekst:
        y=x.split(" - ")
        if y[1]==zanr:
            finallist.append(y[0])
    return(finallist)    
def lisaFilm(nimi,zanr):
    f=open("filmid.txt","a",encoding="utf-8")
    f.write("\n")
    o=nimi+" - "+zanr
    f.write(o)
    f.close()
def kustutaFilm(nimi):
    f=open("filmid.txt","r",encoding="utf-8")
    read=f.readlines()
    f.close()
    f=open("filmid.txt","w",encoding="utf-8")
    for rida in read:
        if rida[0:len(nimi)] != nimi:
            f.write(rida)
    f.close()