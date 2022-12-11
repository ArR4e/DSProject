poisid_ja_tüdrukud = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(poisid_ja_tüdrukud):
    poiste_arv = 0
    tüdrukute_arv = 0
    for rida in poisid_ja_tüdrukud:
        uus_list = rida.split(" ")
        while uus_list.count("P") == True:
            poiste_arv += 1
            break
        else:
            uus_list.count("T")
            tüdrukute_arv += 1
            continue
    return(poiste_arv, tüdrukute_arv)

print(poisse_ja_tüdrukuid(poisid_ja_tüdrukud))
        