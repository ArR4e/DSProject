nimed = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T', "Aleks P"]

def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for järjendi_el in järjend:
        uus_järjend = järjendi_el.split(" ")
        for uus_el in uus_järjend:
            if uus_el == "P":
                poiste_arv += 1
            elif uus_el == "T":
                tüdrukute_arv += 1
            else:
                pass
    return poiste_arv, tüdrukute_arv


print(poisse_ja_tüdrukuid(nimed))                
                
                
   
        
# nimi = "Mati P"
# nimi2 = nimi.split(" ")
# print(nimi2)
        


