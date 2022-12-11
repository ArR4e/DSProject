def väljasta_liin(eellane, järglane, sugupuu):
    if järglane not in sugupuu:
        return(False)
    if eellane in sugupuu[järglane]:
        print(eellane)
        print(järglane)
        return(True)
    else:
        for nimi in sugupuu[järglane]:
            if nimi in sugupuu:
                if väljasta_liin(eellane, nimi, sugupuu)==True:
                    print(järglane)
                    return(True)
            else:
                return(False)
                
                
                

