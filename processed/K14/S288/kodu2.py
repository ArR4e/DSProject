def väljasta_liin(eellane, järglane, sõnastik):
    for i in sõnastik:
        if i == järglane:
            isa, ema = sõnastik[i]
            if eellane == isa or eellane == ema:
                print(eellane)
                print(järglane)
                return True
            elif väljasta_liin(eellane, isa, sõnastik):
                print(järglane)
                return True
            elif väljasta_liin(eellane, ema, sõnastik):
                print(järglane)
                return True
    return False