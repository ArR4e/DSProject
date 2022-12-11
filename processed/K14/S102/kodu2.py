def väljasta_liin(eellane, jarglane, sonastik):
    if eellane==jarglane:
        print(eellane)
        return True
    if jarglane not in sonastik:
        return False
    elif väljasta_liin(eellane, sonastik[jarglane][0], sonastik):
        print(jarglane)
        return True
    elif  väljasta_liin(eellane, sonastik[jarglane][1], sonastik):
        print(jarglane)
        return True
    return False