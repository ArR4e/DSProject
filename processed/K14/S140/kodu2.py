def tõde(eellane, järglane, sugupuu):
    if järglane == eellane:
        return True
    else:
        for i in sugupuu:
            if eellane in sugupuu[i]:
                return tõde(i, järglane, sugupuu)
    return False

def väljasta_liin(eellane, järglane, sugupuu): 
    tõeväärtus = tõde(eellane, järglane, sugupuu)
    if tõeväärtus:
        print(eellane)
        for i in sugupuu:
            if eellane in sugupuu[i]:
                väljasta_liin(i, järglane, sugupuu)
        return True
    return False
