def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(eellane)
        return True
    elif järglane in sõnastik:
        for nimi in sõnastik[järglane]:
            if väljasta_liin(eellane, nimi, sõnastik) == True:
                print (järglane)
                return True
    return False