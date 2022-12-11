järjend = ["Mati P","Kati T","Siim Aleksander P","Jüri P","Veronika T"]


def poisse_ja_tüdrukuid(järjend):
    tüdrukute_arv = 0
    poiste_arv = 0
   
    for element in järjend:
        uus_järjend = element.split(" ")
        nimi = uus_järjend[0:-1]
        sugu = uus_järjend[-1:]
        while sugu[0] == "P":
            poiste_arv +=1
            break
        else:
            tüdrukute_arv +=1
            continue
            
            
    return (poiste_arv, tüdrukute_arv)

print(poisse_ja_tüdrukuid(järjend))