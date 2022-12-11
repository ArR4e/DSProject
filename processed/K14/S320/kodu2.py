def väljasta_liin(eellane, järglane, sõnastik):
    if eellane==järglane:
        print(eellane)
        return True
    if järglane in sõnastik.keys():
        if (väljasta_liin(eellane, sõnastik[järglane][0], sõnastik)):
            print(järglane)
            return True
        if (väljasta_liin(eellane, sõnastik[järglane][1], sõnastik)):
            print(järglane)
            return True
    return False

        
