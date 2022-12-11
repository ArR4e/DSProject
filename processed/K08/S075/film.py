#f=open("filmid.txt", encoding="UTF-8")

def loetleFilmid(zanr):
    f=open("filmid.txt", encoding="UTF-8")
    nimejärjend=[]
    for rida in f:
        if rida.strip().split(" - ")[1]==zanr:
            nimejärjend+=[rida.strip().split(" - ")[0]]
        else:
            pass
    return(nimejärjend)
    f.close()
    
    


def lisaFilm(nimi,zanr):
    f=open("filmid.txt", "a+", encoding="UTF-8")
    f.write("\n"+nimi+" - "+zanr)
    f.close()
    


def kustutaFilm(nimi):
    uus=""
    f=open("filmid.txt", "r+", encoding="UTF-8")
    for rida in f:
        if rida.strip().split(" - ")[0]!=nimi:
            uus=uus+rida
        else:
            pass
    f=open("filmid.txt", "w", encoding="UTF-8")
    f.write(uus)
    f.close()
    



