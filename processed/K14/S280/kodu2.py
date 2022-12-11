# 2. Väljasta liin / RP

sugupuu = {'Urmas': ('Artur', 'Ülle'), 'Artur': ('Meelis', 'Ene'), 'Meelis': ('Siim', 'Niina'), 'Siim': ('Priit', 'Krõõt'), 'Ene': ('Oleg', 'Fatme'), 'Oleg': ('Vello', 'Liidia')}

def väljasta_liin(eellane, järglane, sõnastik):
    
    try:
        if sõnastik[järglane][0] == eellane:
            print(eellane)
            return True
        else:
            try:
                if väljasta_liin(eellane, sõnastik[järglane][0], sõnastik) == True:
                    print(sõnastik[järglane][0])
                    return True
            except:
                True
                
        if sõnastik[järglane][1] == eellane:
            print(eellane)
            return True
        else:
            try:
                if väljasta_liin(eellane, sõnastik[järglane][1], sõnastik) == True:
                    print(sõnastik[järglane][1])
                    return True
                else:
                    return False
            except:
                True
                
    except:
        return False
                 
print("Kas liin leidub?", väljasta_liin('Artur', "Ülle", sugupuu))
print()
print("Kas liin leidub?", väljasta_liin('Liidia', "Urmas", sugupuu))