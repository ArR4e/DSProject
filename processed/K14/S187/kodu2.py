def väljasta_liin(eellane, jarglane, sugupuu):
    if eellane == jarglane:
        print(eellane)
        return True

    for nimi in sugupuu:
        if nimi == jarglane:
            if väljasta_liin(eellane, sugupuu[nimi][0], sugupuu):
                print(jarglane)
                return True
            if väljasta_liin(eellane, sugupuu[nimi][1], sugupuu):
                print(jarglane)
                return True

    return False