liin = []

def väljasta_liin(vanem, laps, sõnastik):
    if leia_liin(vanem, laps, sõnastik) != False:
        print(*liin, sep="\n")
        return True
    else:
        return False

def leia_liin(vanem, laps, sõnastik):
    global liin
    
    if vanem == laps:
        return [laps]
    elif laps not in sõnastik:
        return False
    
    else:
        isa, ema = sõnastik[laps][0], sõnastik[laps][1]
        liin = leia_liin(vanem, isa, sõnastik)
        
        try:
            liin.append(laps)
            return liin
        
        except:
            liin = leia_liin(vanem, ema, sõnastik)
            try:
                liin.append(laps)
                return liin
            except:
                return False