def poisse_ja_tüdrukuid(jarjend):
        vastus = []
        poisse = 0
        tüdrukuid = 0
        for el in jarjend:
            if el[len(el)-1] == "P":
                poisse += 1
            else:
                tüdrukuid += 1
        vastus = (poisse,tüdrukuid)
        return(vastus)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))