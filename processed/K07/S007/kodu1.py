def poisse_ja_tüdrukuid(järjend):
    poisid= 0
    tüdrukud= 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        for el in uus_järjend:
            if el == "P":
                poisid +=1 
            elif el == "T":
                tüdrukud +=1
    return(poisid, tüdrukud)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
