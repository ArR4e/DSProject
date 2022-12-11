def loetleFilmid(z):
    f=open("filmid.txt", "r")
    nimekiri=[]
    for rida in f.readlines():
        if z in rida:
            nimekiri.append(rida[:rida.index(" - ")])
    
    f.close
    return nimekiri
def lisaFilm(n,z):
    f=open("filmid.txt", "a")
    f.write("\n"+n+" - "+z)
    f.close
def kustutaFilm(n):
    f=open("filmid.txt", "r")
    read=f.readlines()
    f.close
    f=open("filmid.txt", "w")
    for rida in read:
        if n in rida:
            koht=read.index(rida)
    del read[koht]
    for rida in read:
        f.write(rida)
            #if read.index(rida)!= len(read)-2:
             #   f.write(rida)
            #else:
             #   f.write(rida.strip("\n"))
        
            
    f.close