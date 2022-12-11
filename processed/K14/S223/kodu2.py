def väljasta_liin(eellane, järglane, sugupuu):
    if järglane == eellane:
        print(eellane)
        return True
    if järglane in sugupuu.keys():
        if väljasta_liin(eellane, sugupuu[järglane][0], sugupuu) or väljasta_liin(eellane, sugupuu[järglane][1], sugupuu):
            print(järglane)
            return True
    return False
    

dict_puu = {'Kalle': ('Teet', 'Maris'),'Maris': ('Konstantin', 'Mari'), 'Rita': ('Teet', 'Maris'), 'Siim': ('Teet', 'Maris'), 'Mari': ('Karl', 'Leeni'), 'Teet': ('Joosep', 'Adele'), 'Adele': ('Johannes', 'Leida'), 'Konstantin': ('Viktor', 'Jelena'), 'Joosep': ('August', 'Emma'), 'Viktor': ('Nikolai', 'Maria')}
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', dict_puu))