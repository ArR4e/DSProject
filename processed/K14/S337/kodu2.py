def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        print(järglane)
        return True
    else:
        for laps in sugupuu:
            if laps == järglane:
                if väljasta_liin(eellane, sugupuu[laps][0], sugupuu) or väljasta_liin(eellane, sugupuu[laps][1], sugupuu):
                    print(laps)
                    return True
    return False