def loetleFilmid(žanr):
    f=open("filmid.txt", encoding="UTF-8")
    järjend=[]
    for rida in f:
        if rida.strip().split(" - ")[1]==žanr:
            järjend+=[rida.strip().split(" - ")[0]]
        else:
            pass
    return(järjend)
    f.colse()
       
def lisaFilm(filmi_nimi, žanr):
    f=open("filmid.txt", "a+", encoding="UTF-8")
    f.write("\n"+filmi_nimi+" - "+žanr)
    f.close
    
def kustutaFilm(filmi_nimi):
    uus=""
    f=open("filmid.txt","r+", encoding="UTF-8")
    for rida in f:
        if rida.strip().split(" - ")[0]!=filmi_nimi:
            uus=uus+rida
        else:
            pass
    f=open("filmid.txt","w", encoding="UTF-8")
    f.write(uus)
    f.close