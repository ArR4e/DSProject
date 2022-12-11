liin=[]
def väljasta_liin( eellane, järglane, sugupuu):
    global liin
    liin.append(eellane)
    järglased=[]
    for järg in sugupuu:
        if eellane in sugupuu[järg]:
            järglased.append(järg)
    if järglane in järglased:
        for nimi in liin:
            print(nimi)
        print(järglane)
        return True
    else:
        for jär in järglased:
            v=väljasta_liin(jär, järglane, sugupuu)
            return v
    return False

