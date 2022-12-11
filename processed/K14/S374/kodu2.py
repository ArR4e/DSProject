def kas_leidub(eellane, jarglane, sugupuu):
    if eellane == jarglane:
        return True
    
    for el in sugupuu:
        eellane1 = sugupuu[el][0]
        eellane2 = sugupuu[el][1]
            
        if eellane == eellane1 or eellane == eellane2:
            return(kas_leidub(el, jarglane, sugupuu))
    return False

        

def väljasta_liin(eellane, jarglane, sugupuu):
    if kas_leidub(eellane, jarglane, sugupuu) == True:
        if eellane == jarglane:
            print(eellane)
        
        for el in sugupuu:
            eellane1 = sugupuu[el][0]
            eellane2 = sugupuu[el][1]
            
            if eellane == eellane1 or eellane == eellane2:
                print(eellane)
                väljasta_liin(el, jarglane, sugupuu)
                return True
    else:
        return False
            
                
                
