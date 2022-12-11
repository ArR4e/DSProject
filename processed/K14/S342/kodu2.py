def väljasta_liin(eellane, järglane, sõnastik):
    uusdict = {}
    for laps, vanemad in sõnastik.items():
        if vanemad in uusdict:
            uusdict[vanemad].append(laps)
        else:
            uusdict[vanemad] = [laps]
    for vanemad in uusdict:
        if eellane != järglane:
            if vanemad[0] == eellane or vanemad[1] == eellane:
                print(eellane)
                return väljasta_liin(uusdict[vanemad][0], järglane, sõnastik)
                try:
                    return väljasta_liin(uusdict[vanemad][1], järglane, sõnastik)
                except:
                    continue
                try:
                    return väljasta_liin(uusdict[vanemad][2], järglane, sõnastik)
                except:
                    continue
        else:
            print(eellane)
            return True

