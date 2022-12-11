

def loetleFilmid(zanr):
    fail  = open("filmid.txt", encoding = "utf-8")
    väljund = []
    for i in fail:
        i = i.strip()
        i = i.split(" - ")
        if i[1] == zanr:
            väljund.append(i[0])
    return väljund

def lisaFilm(nimi,zanr):
    fail = open("filmid.txt","a", encoding = "utf-8")
    rida = nimi +" - " + zanr
    fail.write("\n")
    fail.write(rida)
    fail.close()
    
    
def kustutaFilm(nimi):
    fail = open("filmid.txt",encoding = "utf-8")
    read  = fail.readlines()
    fail.close()
    uusfail = open("filmid.txt","w", encoding = "utf-8")
    for i in read:
        b = i.strip()
        a = b.split(" - ")
        if nimi not in a:
            uusfail.write(i)
    uusfail.close()

