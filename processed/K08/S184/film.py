def loetleFilmid(z):
    f=open("filmid.txt", encoding="UTF-8")
    a=f.readlines()
    b=[]
    for c in a:
        if z not in c.strip("\n"):
            continue
        else:
            d=c.strip("\n").split("-")
            b=b+[d[0].strip(" ")]
    f.close()
    print(b)
    return b
    
def lisaFilm(nimi, zanr):
    f=open("filmid.txt", encoding="UTF-8")
    read=f.readlines()
    f.close()
    
    f2=open("filmid.txt", "w", encoding="UTF-8")
    b="\n"+nimi+" - "+zanr
    read.append(b)
    for i in read:
        f2.write(i)
    f2.close()
    return 
    
def kustutaFilm(n):
    f=open("filmid.txt", encoding="UTF-8")
    read=f.readlines()
    f.close()
    
    f2=open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if n not in rida.strip("\n"):
            f2.write(rida)
        else:
            continue 
    f2.close()
    return

