
def väljasta_liin(eellane,järglane,sõn):
    if järglane in sõn:
        for nimi in sõn[järglane]:
            if nimi == eellane:
                print(nimi)
                print(järglane)
                return True
            else:
                if väljasta_liin(eellane, nimi,sõn) == True:

                    print(järglane)
                    return True
                
    return False      
    
