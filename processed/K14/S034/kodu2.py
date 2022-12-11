def väljasta_liin(eellase_nimi,järglase_nimi,sõnastik,järjend=[]):
    järjend += [eellase_nimi]
    for võti,väärtus in sõnastik.items():
        if väärtus[0] == eellase_nimi or väärtus[1] == eellase_nimi:
            if  võti == järglase_nimi:
                järjend += [võti]
                for element in järjend:
                        print(element)
                return True
            else:
                tõde = väljasta_liin(võti,järglase_nimi,sõnastik,järjend)
                return tõde
    else:
        return False