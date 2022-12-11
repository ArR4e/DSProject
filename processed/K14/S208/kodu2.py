def väljasta_liin(eellane, järglane, sugupuu):
    if järglane in sugupuu:
        for el in sugupuu[järglane]:
            if el == eellane:
                print(eellane)
                print(järglane)
                return True
            elif el in sugupuu:
                if väljasta_liin(eellane, el, sugupuu) == True:
                    print(järglane)
                    return True
    return False