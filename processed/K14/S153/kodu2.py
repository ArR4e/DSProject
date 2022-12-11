def väljasta_liin(eellane, järglane, sugupuu):
    if kasvaluedes(eellane, sugupuu) == True:
        uus_eellane = sugupuu[järglane]
        while uus_eellane != järglane:
                väljasta_liin(uus_eellane, järglane, sugupuu)
        else:
            return True
    else:
        return False

def kasvaluedes(nimi, sugupuu):
    vanemad = list(sugupuu.values())
    for isa, ema in vanemad:
        if nimi == isa or nimi == ema:
            koht = sugupuu[nimi]
            return True
        else:
            continue
print(kasvaluedes("Leida", sugupuu))
print(väljasta_liin("Leida", "Kalle", sugupuu))