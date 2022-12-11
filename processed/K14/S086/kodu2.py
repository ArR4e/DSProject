

def väljasta_liin(eellane, järglane, sugupuu):
    if järglane in sugupuu.keys():
        for nimi in sugupuu[järglane]:
            if nimi == eellane:
                print(nimi)
                print(järglane)
                return True
            elif väljasta_liin(eellane, nimi, sugupuu):
                print(järglane)
                return True
        return False
    return False