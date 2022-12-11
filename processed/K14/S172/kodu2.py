def väljasta_liin(eellane, jarglane, sugupuu):
    if jarglane not in sugupuu.keys():
        return False
    elif eellane in sugupuu[jarglane]:
        print(eellane)
        print(jarglane)
        return True

    a = väljasta_liin(eellane, sugupuu[jarglane][0], sugupuu)
    b = väljasta_liin(eellane, sugupuu[jarglane][1], sugupuu)
    
    if a != False:
        return a
    else:
        return b
    