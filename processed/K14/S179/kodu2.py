def väljasta_liin(eellane, järglane, sugupuu):
    if järglane == eellane:
        print(järglane)
        return True
    elif järglane not in sugupuu:
        return False
    elif väljasta_liin(eellane,sugupuu[järglane][0], sugupuu) == True:
        print(järglane)
        return True
    elif väljasta_liin(eellane,sugupuu[järglane][1], sugupuu) == True:
        print(järglane)
        return True
    else:
        return False
