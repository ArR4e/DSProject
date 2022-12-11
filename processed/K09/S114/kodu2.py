import random
#Osa kodu2 ülesande lahendamise logist läks kaduma, sest Thonny jooksis kokku ja logi ei tekkinud
def minu_shuffle(järjend):
    kasutatudnumbrid = []
    uuslist = järjend[:]
    listipikkus = len(järjend)
    Tsükklitearv = 0
    
    while True: #uue suvalise järjekorra loomine indeksitele
        if järjend == []:
            break
        juhuslikNumber = random.randint(1,listipikkus)
        if Tsükklitearv == listipikkus:
            break
        if (juhuslikNumber-1) in kasutatudnumbrid:
            continue
        else:
            kasutatudnumbrid.append(juhuslikNumber-1)

        Tsükklitearv += 1
        
    #Uue asukoha määramine
    Tsükklitearv = 0
    while Tsükklitearv < listipikkus:
        järjend[Tsükklitearv] = uuslist[kasutatudnumbrid[Tsükklitearv]]
        Tsükklitearv += 1
