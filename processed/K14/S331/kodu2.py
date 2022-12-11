def väljasta_liin(eellasenimi, järglasenimi, sõnastik):
    x = 0
    if eellasenimi == järglasenimi:
        print(eellasenimi)
        return True
    if järglasenimi in sõnastik:
        eellane_isa = sõnastik[järglasenimi][0]
        eellane_ema = sõnastik[järglasenimi][1]
        if väljasta_liin(eellasenimi, eellane_isa, sõnastik):
            x += 1
            print(järglasenimi)
            return True
        if väljasta_liin(eellasenimi, eellane_ema, sõnastik):
            x += 1
            print(järglasenimi)
            return True
    if x == 0:
        return False
        

           
            