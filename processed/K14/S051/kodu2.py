def väljasta_liin(eellane, järglane, sugupuu):
    if eellane is järglane:
        print(järglane)
        return True
    elif järglane in sugupuu:
        for nimi in sugupuu[järglane]:
            if väljasta_liin(eellane, nimi, sugupuu):
                print(järglane)
                return True
    return False