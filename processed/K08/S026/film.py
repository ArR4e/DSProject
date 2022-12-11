file = open("filmid.txt", encoding = "utf-8")


def loetleFilmid(zanrid):
    teemad = []
    filmid = []
    see_zanr = []
    
    for rida in file:
        rida = rida.strip()
        pooleks = rida.split(" - ")
    
        film = pooleks[0]
        zanr = pooleks[1]
    
        teemad += [zanr]
        filmid += [film]
    
    pos = -1
    for element in range (len(teemad)):
        if teemad[element] == zanrid:
            pos = element
            for i in teemad:
                if zanrid == "":
                    break
                if zanrid == i:
                    if pos != -1:
                        see_zanr += [filmid[pos]]
                        print(see_zanr)
            
loetleFilmid("multikas")

file.close()

#ma ei saa seda tööle. Ma ei suuda välja mõelda, miks ta mitu korda seda läbi teeb.
            