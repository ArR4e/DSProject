def väljasta_liin(eellane, järglane, sõnastik, liin=[]):
    if järglane not in sõnastik.keys():
        return False
    else:
        for el in sõnastik:
            if eellane in sõnastik[el]:
                uus_eel = el
                if eellane not in liin:
                    liin.append(eellane)
                väljasta_liin(uus_eel, järglane, sõnastik,)
                if liin[-1] in sõnastik[järglane]:
                    if järglane not in liin:
                        liin.append(järglane)
    if liin[-1] == järglane:
        print(liin)
        return True
    else:
        return False