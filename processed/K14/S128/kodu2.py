#Väljasta liin
liin = []
def väljasta_liin(eellane, järglane, sugupuu):
    if järglane not in sugupuu.keys():
        pass
    else:
        vanemad = sugupuu[järglane]
        if eellane == vanemad[0] or eellane == vanemad[1]:
            liin.append(eellane)
            liin.append(järglane)
        else:
            for nimi in sugupuu.keys():
                for vanem in sugupuu[nimi]:
                    if vanem == eellane:
                        liin.append(eellane)
                        return väljasta_liin(nimi, järglane, sugupuu)
    if järglane not in sugupuu.keys():
        return False
    else:
        if eellane == vanemad[0] or eellane == vanemad[1]:
            for el in liin:
                print(el)
            return True
        else:
            return False
