jär = []
def väljasta_liin(eellane, järglane, sõnastik):
    jär.append(eellane)
    if järglane not in sõnastik:
        return False
    elif eellane in sõnastik[järglane]:
        jär.append(järglane)
        for i in jär:
            print(i)
        return True
    else:
        for i in sõnastik:
            if eellane in sõnastik[i]:
                uuseel = i
                break
        try:
            return väljasta_liin(uuseel, järglane, sõnastik)
        except:
            return False