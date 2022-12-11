#f=open("filmid.txt", "r",encoding='utf-8' )

def loetleFilmid(liik):
    f=open("filmid.txt", "r",encoding='utf-8' )
    järjend=[]
    for rida in f:
        if liik== "multikas" and rida.endswith("multikas\n"):
            rida=rida.split(" - ")
            järjend.append(rida[0])
            continue
        elif liik== "märul" and rida.endswith("märul\n"):
            rida=rida.split(" - ")
            järjend.append(rida[0])
            continue
        elif liik== "õudukas" and rida.endswith("õudukas\n"):
            rida=rida.split(" - ")
            järjend.append(rida[0])
            continue
    return järjend
def lisaFilm(nimi, liik):
    f=open("filmid.txt", "a+",encoding='utf-8' )
    f.write('\n') 
    str(nimi)
    str(liik)
    uus=str(nimi + " - " + liik)
    f.write(uus)

def kustutaFilm(nimi):
    f=open("filmid.txt", "r+",encoding='utf-8' )
    for rida in f:
        rida=rida.split(" - ")
        if rida[0]==nimi:
            #for riida in f:
            if f.find(rida)!= 1:
                f.write("")
                break
        else:
            continue

#loetleFilmid("märul")
#lisaFilm("peeterontont", "õudukas")
#kustutaFilm("peeter")
#f.close()