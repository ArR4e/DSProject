def väljasta_liin(eellane, järglane, sugupuu):
    if järglane in sugupuu:
        if eellane in sugupuu[järglane]:
            print(eellane)
            print(järglane)
            
            return True
        else:
            if väljasta_liin(eellane, sugupuu[järglane][0], sugupuu) or väljasta_liin(eellane, sugupuu[järglane][1], sugupuu):
                print(järglane)
                
                return True
            else:
                return False
    else:
        return False