def võitja(mänguväli):
    ristide_arv=0
    ringide_arv=0
    for rida in range(len(mänguväli)):
        see_rida = mänguväli[rida]
        #3 ühes reas
        for veerg in range(len(see_rida)-2):
            if see_rida[veerg] == "X" and see_rida[veerg+1] == "X" and see_rida[veerg+2] == "X":
                ristide_arv += 1
            elif see_rida[veerg] == "O" and see_rida[veerg+1] == "O" and see_rida[veerg+2] == "O":
                ringide_arv += 1
            if len(mänguväli) - rida > 2:
                järgmine_rida = mänguväli[rida+1]
                ülejärgmine_rida = mänguväli[rida+2]
                #3 ühes veerus
                if see_rida[veerg] == "X" and järgmine_rida[veerg] == "X" and ülejärgmine_rida[veerg] == "X":
                    ristide_arv += 1
                elif see_rida[veerg] == "O" and järgmine_rida[veerg] == "O" and ülejärgmine_rida[veerg] == "O":
                    ringide_arv += 1
                if len(see_rida) - veerg > 2:
                    #3 "laskuvas" diagonaalis
                    if see_rida[veerg] == "X" and järgmine_rida[veerg+1] == "X" and ülejärgmine_rida[veerg+2] == "X":
                        ristide_arv += 1
                    elif see_rida[veerg] == "O" and järgmine_rida[veerg+1] == "O" and ülejärgmine_rida[veerg+2] == "O":
                        ringide_arv += 1
                    #3 "tõusvas" diagonaalis
                    if see_rida[veerg+2] == "X" and järgmine_rida[veerg+1] == "X" and ülejärgmine_rida[veerg] == "X":
                        ristide_arv += 1
                    elif see_rida[veerg+2] == "O" and järgmine_rida[veerg+1] == "O" and ülejärgmine_rida[veerg] == "O":
                        ringide_arv += 1
    sõnastik = {}
    sõnastik["X"] = ristide_arv
    sõnastik["O"] = ringide_arv
    return sõnastik

