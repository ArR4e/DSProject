fail = open("filmid.txt")
žanrinimi = input()
žanrite_järjend = []
#1
def loetleFilmid(žanrinimi):
    with open("filmid.txt") as fail:
        for rida in fail:
            f = rida.strip().split(" - ")
        
            if žanrinimi == "multikas" and f[-1] == "multikas":
                žanrite_järjend.append(f[0])
            elif žanrinimi == "märul" and f[-1] == "märul":
                žanrite_järjend.append(f[0])
            elif žanrinimi == "õudukas" and f[-1] == "õudukas":
                žanrite_järjend.append(f[0])
                continue
    return(žanrite_järjend)

#2
def lisaFilm(filmiNimi, filmiŽanr):
    #https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
    with open("filmid.txt", "a") as fail:
        juurde = "\n" + filmiNimi + " - " + filmiŽanr
        fail.write(juurde)
    
#3
def kustutaFilm(film):
    rida = 0
    fail = open("filmid.txt", "r")
    tühi = ""
    for rida in fail:
        if film in rida:
            continue
        else:
            tühi += rida
    fail.close()
    fail = open("filmid.txt", "w")
    fail.write(tühi)
    return(tühi)

fail.close()