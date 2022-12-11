def väljasta_liin(eellane, järglane, sõnastik):
    for jarg, eel in sõnastik.items():
        if järglane == jarg:
            isa, ema = eel
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