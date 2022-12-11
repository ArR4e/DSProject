def väljasta_liin(eellane, jarglane, sugupuu):
    if jarglane in sugupuu and eellane in sugupuu[jarglane]:
        print(eellane)
        print(jarglane)
        return True
    elif jarglane in sugupuu and väljasta_liin(eellane, sugupuu[jarglane][0], sugupuu):
        print(jarglane)
        return True
    elif jarglane in sugupuu and väljasta_liin(eellane, sugupuu[jarglane][1], sugupuu):
        print(jarglane)
        return True
    return False