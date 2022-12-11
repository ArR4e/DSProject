def loetleFilmid (nimi):
    f=open("filmid.txt",encoding="UTF-8")
    vastus=[]
    for rida in f.readlines():
        rida=rida.strip("\n")
        rida=rida.split(" - ")
        if nimi in rida:
            vastus.append(rida[0])
    f.close()
    return vastus
def lisaFilm (nimi, zanr):
    f=open("filmid.txt","w")
    print(nimi+" - "+zanr,file=f)
    f.close()
def kustutaFilm (nimi):
    f=open("filmid.txt","r")
    sisu=f.readlines()
    f.close()
    f=open("filmid.txt","w")
    for a in range(len(sisu)):
        try:
            sisu[a]=sisu[a].strip("\n")
            sisu[a]=sisu[a].split(" - ")
            if nimi in sisu[a]:
                sisu[a].pop()
        except:
            break
    for a in sisu:
        print(a[0],"-",a[1],file=f)
    f.close()