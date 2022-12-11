def väljasta_liin(eellane, järglane, sugupuu, sugulased=[]):
    alg_eellane=järglane
    if järglane==eellane:
        sugulased.append(järglane)
        if järglane==alg_eellane:
            print(sugulased)
            return True
    else:
        if järglane not in sugupuu.keys():
            return False
        else:
            for i in sugupuu[järglane]:
                väljasta_liin(eellane, i, sugupuu)
                if sugulased==[]:
                    continue
                if  järglane not in sugulased:
                    sugulased.append(järglane)
                    if järglane==alg_eellane:
                        print(sugulased)
                        return True  
                        
    if sugulased==[]:
        return False


