
def väljasta_liin(eelane, järglane, sõnastik):
    
    if eelane == järglane:
        print(järglane)
        return True
    elif järglane not in sõnastik.keys():
        return False
    else:
        isa = väljasta_liin(eelane, sõnastik[järglane][0],sõnastik)
        ema = väljasta_liin(eelane, sõnastik[järglane][1],sõnastik)
        if ema:
            print(järglane)
        if isa:
            print(järglane)
        return isa or ema
        

    