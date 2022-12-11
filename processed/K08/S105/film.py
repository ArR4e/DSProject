f=open("filmid.txt", encoding="UTF-8")
failisisu=""

for rida in f:
    rida=rida.strip()
    failisisu+=rida
    failisisu+=" - "

f.close()
    
filmid=[]
filmid=failisisu.split(" - ")

def loetleFilmid(a):
    filmid_zanrist=[]
    i=0
    for ele in filmid:
        i+=1
        if ele == a:
            filmid_zanrist.append(filmid[i-2])
    return filmid_zanrist

def lisaFilm(a,b):
    f=open("filmid.txt","a", encoding="UTF-8")
    f.write("\n")
    f.write(a)
    f.write(" - ")
    f.write(b)
    f.close()
    
def kustutaFilm(a):
    f=open("filmid.txt","r", encoding="UTF-8")
    sisu=""
    for rida in f:
        if a in rida:
            continue
        else:
            sisu+=rida
            
    f=open("filmid.txt","w", encoding="UTF-8")
    f.write(sisu)
    f.close()