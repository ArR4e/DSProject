#Funktsioon poisid ja tudrukud
def poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tüdrukud = 0
#For loop soo leidmiseks jarjendist
    for sugu in nimed:
        if sugu[-1] == "P":
            poisid += 1
        else:
            tüdrukud += 1
    return(poisid, tüdrukud)

#List nimedega
nimed = ["Mati P", "Kati T", "Siim Aleksander P", "Juri P", "Veronika T"]

#Funktisooni valjakutsumine
poisse_ja_tüdrukuid(nimed)
#Vastuse valjastamine
print(poisse_ja_tüdrukuid(nimed))

    