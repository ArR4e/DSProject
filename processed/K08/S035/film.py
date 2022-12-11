def loetleFilmid(žanr):
    f=open("filmid.txt", encoding="UTF-8")
    loetelu=[]
    for rida in f:
        a=rida.split(" - ")
        if žanr in rida: 
            loetelu.append(a[0])
    return(loetelu)
    f.close()
def lisaFilm(nimi, žanr):
    f=open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + str(nimi) + " - " + str(žanr))
    f.close()
def kustutaFilm(filmi_nimi):
    f=open("filmid.txt", encoding="UTF-8")
    read=f.readlines()
    f.close()
    uus=open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if filmi_nimi not in rida.strip("\n"):
            uus.write(rida)
    uus.close()


        