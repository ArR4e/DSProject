def väljasta_liin(eellane,järglane,sugupuu,liin=[]):
    if järglane==eellane:
        for i in liin:
            print(i)
        print(eellane)
        return True
    for i in sugupuu:
        if eellane==sugupuu[i][0] or eellane==sugupuu[i][1]:
            liin.append(eellane)
            return väljasta_liin(i,järglane,sugupuu,liin)
    return False