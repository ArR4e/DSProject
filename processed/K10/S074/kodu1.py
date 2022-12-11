#Erinevad sumbolid funktsioon
def erinevad_sümbolid(sümbolid):
    erinevad = set(sümbolid)
    return erinevad
#Sumbolite sageduse funktisoon
def sümbolite_sagedus(sagedus):
    sagedus1 = {}
    for el in sagedus:
        if el in sagedus1:
            sagedus1[el] = sagedus1[el] + 1
        else:
            sagedus1[el] = 1
    return sagedus1
#Grupeerimise funktsioon
def grupeeri(hulk):
    #Tais- ja kaashaalikud
    täishäälikud = ("a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü")
    kaashäälikud = ("b","d","f","g","h","j","k","l","m","n","p",
                    "r","s","š","z","ž","t","v","q","w","x","y","c",
                    "B","D","F","G","H","J","K","L","M","N","P","R",
                    "S","Š","Z","Ž", "T","V","Q","W","X","Y","C")
    #Tuhjad sonastikud
    täishääl = {}
    kaashääl = {}
    muudmärgid = {}
    #For loop sonastike jaoks 
    for el in hulk:
        #Taishaalikud
        if el in täishäälikud:
            if el in täishääl:
                täishääl[el] = täishääl[el] + 1
            else:
                täishääl[el] = 1
        #Kaashaalikud
        elif el in kaashäälikud:
            if el in kaashääl:
                kaashääl[el] = kaashääl[el] + 1
            else:
                kaashääl[el] = 1
        #Muudmargid
        else:
            if el in muudmärgid:
                muudmärgid[el] = muudmärgid[el] +1
            else:
                muudmärgid[el] = 1
    täis = set(täishääl.items())
    kaas = set(kaashääl.items())
    muud = set(muudmärgid.items())
    return {"Täishäälikud" : täis, "Kaashäälikud" : kaas, "Muud" : muud}

#Esimesed kaks funktsiooni on tehtud iseseisvalt
#Grupeerimise funktsiooniga kusisin natuke abi kurusekaaslaselt

#print(erinevad_sümbolid("siin ei ole korduvaid märke"))
#print(sümbolite_sagedus("asdasdasdferg"))
#print(grupeeri("kuu-uurija"))
                