def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(d + [järglane])
        return True

    else:
        for laps, vanemad in sõnastik.items():
            if eellane in vanemad:
                d.append(eellane)
                return väljasta_liin(laps, järglane, sõnastik)
        return False

d = []  