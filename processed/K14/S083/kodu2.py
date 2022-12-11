def väljasta_liin(eellane, järglane, sõnastik):
    if järglane in sõnastik:
        if eellane in sõnastik[järglane]:
            print(eellane)
            print(järglane)
            return True
        else:
            for vanem in sõnastik[järglane]:
                if väljasta_liin(eellane, vanem, sõnastik) == True:
                    print(järglane)
                    return True
            return False
    else:
        return False
