def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(eellane)
        return True
    if järglane in sõnastik:
        for vanem in sõnastik[järglane]:
            if väljasta_liin(eellane, vanem, sõnastik):
                print(järglane)
                return True
    return False
