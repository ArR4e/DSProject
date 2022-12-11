def väljasta_liin(eellane, järglane, sõnastik, järjend = []):
    
    if eellane == järglane:
        järjend.append(eellane)
        for nimi in järjend:
            print(nimi)
    
    for laps, vanemad in sõnastik.items():
        if eellane in vanemad:
            järjend.append(eellane)
            väljasta_liin(laps,järglane,sõnastik, järjend)

    if järglane in järjend:
        return True
    else:
        return False

