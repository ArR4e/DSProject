def loetleFilmid(zanr):
    f = open("filmid.txt","r", encoding = "UTF = 8")
    loetud = f.read()
    f.close()
    
    loetud = loetud.replace("\n"," - ")
    loetud = loetud.split(" - ")
    
    sobivad = []

    for i in range(len(loetud)):
        if i % 2 == 0:
            continue
        elif loetud[i] == zanr:
            sobivad.append(loetud[i-1])
    return sobivad
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt","a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + zanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    järjend = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding = "UTF-8")
    
    for i in järjend:
        if nimi not in i:
            f.write(i)
    f.close()
    
