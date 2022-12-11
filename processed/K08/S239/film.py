def loetleFilmid(žanr):
    f=open("filmid.txt",encoding="UTF8")
    read=f.readlines()
    f.close()
    
    loetelu = []
    for rida in read:
        if len(rida.strip("\n").split(" - ")) == 1:
            break
        if rida.strip("\n").split(" - ")[1] == žanr:
            loetelu.append(rida.strip("\n").split(" - ")[0])
    return loetelu

def lisaFilm(film,žanr):
    f=open("filmid.txt","a",encoding="UTF8")
    f.write("\n"+film+" - "+žanr)
    f.close()

def kustutaFilm(film):
    f=open("filmid.txt",encoding="UTF8")
    read=f.readlines()
    f.close()

    for rida in read:
        if rida.strip("\n").split(" - ")[0] == film:
            read.remove(rida)
            
    f=open("filmid.txt","w",encoding="UTF8")
    for rida in read:
        f.write(rida)
    f.close()

lisaFilm("Lotte reis lõunamaale","märul")
kustutaFilm("Lotte reis lõunamaale")
print(loetleFilmid("märul"))