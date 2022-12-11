def väljasta_liin(eellane, järglane, sugupuu):
    if järglane not in sugupuu:
        return False
    else:
        for rida in sugupuu:
            if sõnastik[rida][0] == eellane:
                print(eellane)
                väljasta_liin(rida,järglane,sõnastik)
            elif sõnastik[rida][1] == eellane:
                print(eellane)
                väljasta_liin(rida,järglane,sõnastik)
    print(järglane)
    return True
                
        
                        
sõnastik = {}

print("Kas liin leidub?", väljasta_liin("Leida","Kalle",sõnastik))