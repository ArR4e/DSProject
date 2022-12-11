def väljasta_liin(enimi, jnimi, sugupuu):
    if sugupuu == {}:
        return False
    if not jnimi in sugupuu.keys():
        return False
    if enimi in sugupuu[jnimi]:
        print(enimi)
        print(jnimi)
        return True
    else:
        eellased = sugupuu.pop(jnimi)
        if väljasta_liin(enimi,eellased[0], sugupuu):
            print(jnimi)
            return True
        if väljasta_liin(enimi,eellased[1], sugupuu):
            print(jnimi)
            return True
        return False