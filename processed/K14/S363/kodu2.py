def väljasta_liin(eellane, järglane, sugupuu, eellased=[]):
    if järglane in sugupuu.keys():
        if eellane in sugupuu[järglane]:
            for nimi in eellased:
                print(nimi)
            print(eellane + "\n" + järglane)
            return True
    else:
        return False    
    
    for nimi in sugupuu.keys():
        if eellane in sugupuu[nimi]:
            eellased.append(eellane)
            return väljasta_liin(nimi, järglane, sugupuu, eellased)
    
    return False

