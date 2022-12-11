#kas järglane on vanemate kaudu põlvnenud eellasest

def väljasta_liin(eellane, järglane, sõnastik):
    for järg, eel in sõnastik.items():
        if järg==järglane:
            isa,ema = eel
            if eellane==isa or eellane==ema:
                print(eellane)
                print(järglane)
                return True
            elif väljasta_liin(eellane, isa, sõnastik):
                print(järglane)
                return True
            elif väljasta_liin(eellane, ema, sõnastik):
                print(järglane)
                return True
                    
                    
    else:
        return False

