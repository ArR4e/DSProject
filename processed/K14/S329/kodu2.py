# 2. Väljasta liin

def väljasta_liin(enimi, jnimi, sõnastik):
    if jnimi in sõnastik:
        for el in range(2):
            if sõnastik[jnimi][el] == enimi:
                print(enimi)
                print(jnimi)
                return True
            else:
                if väljasta_liin(enimi, sõnastik[jnimi][el], sõnastik) == True:
                    print(jnimi)
                    return True
    return False
    
    
    
    
    
#sõnastik = {'Kalle': ('Teet', 'Maris'), 'Maris': ('Konstantin', 'Mari'), 'Rita': ('Teet', 'Maris'),
#            'Siim': ('Teet', 'Maris'), 'Mari': ('Karl', 'Leeni'), 'Teet': ('Joosep', 'Adele'),
#            'Adele': ('Johannes', 'Leida'), 'Konstantin': ('Viktor', 'Jelena'), 'Joosep': ('August', 'Emma'),
#            'Viktor': ('Nikolai', 'Maria')}

#print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))