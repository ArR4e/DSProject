def väljasta_liin(eellane, järglane, sugupuu):
    for võti in sõnastik:
        if eellane in sõnastik[võti]:
            nimed.append(eellane)
            eellane = võti
            
            if võti == järglane:
                nimed.append(võti)
                
                for nimi in nimed:
                    print(nimi)
                    
            return väljasta_liin(eellane, järglane, sugupuu)
        
    if järglane in nimed:
        return True
    else:
        return False

nimed = []
sõnastik = {'Kalle': ('Teet', 'Maris'),
            'Maris': ('Konstantin', 'Mari'),
            'Rita': ('Teet', 'Maris'),
            'Siim': ('Teet', 'Maris'),
            'Mari': ('Karl', 'Leeni'),
            'Teet': ('Joosep', 'Adele'),
            'Adele': ('Johannes', 'Leida'),
            'Konstantin': ('Viktor', 'Jelena'),
            'Joosep': ('August', 'Emma'),
            'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
