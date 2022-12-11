

def poisse_ja_tüdrukuid(järjend):
    x=0
    poisse=0
    tüdrukuid=0
    while True:
        try:
            inimene=järjend[x].split(" ")
            x+=1

            for i in inimene:
                if i=="P":
                    poisse=1+poisse
                if i=="T":
                    tüdrukuid=1+tüdrukuid
        except:
            break
    andmed=(poisse,tüdrukuid)
    return(andmed)
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
    
