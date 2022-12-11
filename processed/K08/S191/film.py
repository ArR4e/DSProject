def loetleFilmid(tüüp):
    tüüp_filmid=[]
    f=open("filmid.txt")
    for i in f:
        listed=i.split(" - ")
        if listed[1]==tüüp or listed[1]==str(tüüp)+"\n":
            tüüp_filmid+=listed
            try:
                tüüp_filmid.remove(str(tüüp))
            except:
                pass
            try:
                tüüp_filmid.remove(str(tüüp)+"\n")
            except:
                pass
    return tüüp_filmid

def lisaFilm(nimi, tüüp):
    f=open("filmid.txt","a")
    f.write("\n"+str(nimi)+" - "+str(tüüp))
    f.close()

def kustutaFilm(nimi):
    f=open("filmid.txt")
    read=f.readlines()
    f.close()
    kustutatud=[]
    for i in read:
        if i.startswith(str(nimi)):
            pass
        else:
            kustutatud+=[i]
    f=open("filmid.txt","w")
    for i in kustutatud:
        f.write(i)
    f.close()