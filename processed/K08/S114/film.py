


def loetleFilmid(zanr):
    nimekiri = [] 
    nimekiri2 = [] #Nimekiri ilma \n-ta
    TsükkliteArv = 0
    VäljastatavNimekiri = ""
    ÜhtneJärjend = []
    tere = 0
    f1 = open("filmid.txt","r",encoding = "UTF-8")
    for i in f1:
        if zanr in i:
            nimekiri.append(i)
    for e in nimekiri:
        nimekiri2.append(e.strip().replace(" - ",".").split(".")) #Newline märgi eemaldamine
        ÜhtneJärjend = sum(nimekiri2,[])
    while TsükkliteArv < len(ÜhtneJärjend):
        VäljastatavNimekiri = str(VäljastatavNimekiri) + str(ÜhtneJärjend[TsükkliteArv])
        
        if (len(ÜhtneJärjend)-TsükkliteArv) > 2:
            VäljastatavNimekiri = str(VäljastatavNimekiri)+","
        TsükkliteArv += 2
    tere = VäljastatavNimekiri.split(",")
    f1.close()
    if tere == ['']:
        tere.clear()
    return tere
    
    
def lisaFilm(nimi,zanr):
    tekst = ""
    f1 = open("filmid.txt","a",encoding ="UTF-8")
    if len(nimi) > 1:
        tekst = tekst.join(nimi)
        f1.write("\n"+str(tekst)+" - "+str(zanr))
    else:
        f1.write("\n"+str(nimi)+" - "+str(zanr))
    f1.close()
    
    
def kustutaFilm(nimi):
    f1 = open("filmid.txt","r",encoding ="UTF-8")
    read = f1.readlines()
    f1.close()
    f1 = open("filmid.txt","w",encoding="UTF-8")
    for i in read:
        if nimi not in i:
            f1.write(i)
            
    f1.close()

