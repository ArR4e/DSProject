def loetleFilmid(zanr):
    loend=[]
    lo=[]
    vastav=[]
    i=0
    f1=open("filmid.txt","r",encoding="utf8")
    for rida in f1:
        loend.append(rida.strip("\n").split(" - "))
    for e in loend:
        lo+=e
    while i < len(lo):
        if lo[i] == str(zanr):
            vastav.append(lo[i-1])
        i+=1
    f1.close()
    return vastav

def lisaFilm(nimi,zanr):
    f2=open("filmid.txt","a",encoding="utf8")
    f2.write("\n"+str(nimi)+" - "+str(zanr))
    f2.close()

def kustutaFilm(nimi):
    sisu=[]
    sisu2=[]
    ey=0
    lause=''
    i=0
    fail=open("filmid.txt","r+",encoding="utf8")
    for el in fail:
        sisu.append(el.strip("\n").split(" - "))
    for e in sisu:
        sisu2 += e
    while i < len(sisu2):
        if sisu2[i] == str(nimi):
            print(i)
            teine=sisu2[i+1]
            sisu2.remove(nimi)
            sisu2.pop(i)
        i+=1
    while ey != len(sisu2):
        if ey != len(sisu2)-2:
            lause+= str(sisu2[ey])+" - "+str(sisu2[ey+1])+"\n"
        elif ey == len(sisu2)-2:
            lause+= str(sisu2[ey])+" - "+str(sisu2[ey+1])
        ey+=2
    f3=open("filmid.txt","w",encoding="utf8")
    f3.write(lause)
    f3.close()