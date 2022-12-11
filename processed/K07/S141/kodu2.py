tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", "r")

from math import inf
odavaim = inf
odav_takso_nimi = ""
for i in fail:
    järjend = i.split("\n")

    for i in järjend:
        if i == "":
            break
        else:
            uus = i.split(",")
            takso_nimi = str(uus[0])
            sisseistumise_hind = float(uus[1])
            kilomeetri_hind = float(uus[2])
            hind = sisseistumise_hind + kilomeetri_hind * tee_pikkus
                        
            if hind < odavaim:
                odav_takso_nimi = takso_nimi
                odavaim = hind
                
print("Kõige odavam on " + str(odav_takso_nimi) + ".")