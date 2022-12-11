
def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        return 
    else:
        for isik in sugupuu:
            if eellane in sõnastik[isik]:
                print(isik)
                väljasta_liin(isik, järglane, sugupuu)
                return
