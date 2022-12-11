def loetleFilmid(zanr):
    f = open("filmid.txt","r", encoding="UTF-8")
    filmid = []
    for rida in f:
        rida = rida.strip()
        a = rida.split(' - ')
        if a[1] == zanr:
            filmid = filmid + [a[0]]
    if filmid == []:
        print("Valitud zanri filme ei leitud")
    f.close()
    return filmid
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a")
    f.write("\n"+nimi+" - "+zanr+"\n")
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt","r")
    read = f.readlines()
    u = open("filmid.txt","w")
    for rida in read:
        rida = rida.strip()
        a = rida.split(" - ")
        if a[0] != nimi:
            #u = open("filmid.txt","w")
            u.write(rida+"\n")
    u.close()
    f.close()
        