f=open("filmid.txt","r+",encoding="UTF-8")
filmid=[]
for rida in f:
    a=rida.split(" - ")
    a[1]=a[1].rstrip()
    filmid.append(a)
def loetleFilmid(sisend):
    e=[]
    for rida in filmid:
        if rida[1]==sisend:
            e.append(rida[0])
    return e
def lisaFilm(nimi,t):
    f.close()
    f=open("filmid.txt","w")
    for rida in filmid:
        f.write(str(rida[0]+" - "+rida[1]+"\n"))
    f.write(str(nimi)+" - "+str(t)+"\n")
    f.close()
def kustutaFilm(nimi):
    f=open("filmid.txt","w")
    for rida in filmid:
        if rida[1]==nimi:
            f.write("/n")
        else:
            f.write(str(rida[0])+" - "+str(rida[1])+"\n")
            
    f.close()
