def loetleFilmid(žanr):
    f=open("filmid.txt",encoding="UTF-8")
    filmid=[]
    for i in f:
        i=i.strip().split(" - ")
        if i[1]==žanr:
            filmid+=[i[0]]
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    f=open("filmid.txt","a",encoding="UTF-8")
    f.write(f"\n {nimi} - {žanr}")
    f.close()
    
def kustutaFilm(nimi):
    f=open("filmid.txt","r",encoding="UTF-8")
    read=f.readlines()
    f.close()
    f=open("filmid.txt","w",encoding="UTF-8")
    a=0
    for rida in read:
        i=rida.strip().split(" - ")
        if i[0] == nimi:
            continue
        if a==0:
            f.write(rida.strip("\n"))
            a=1
        else:
            f.write("\n"+rida.strip("\n"))
    f.close()