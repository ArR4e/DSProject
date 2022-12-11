def väljasta_liin(eellane, järglane, sõnastik):
    tõeväärtus = False
    if eellane == järglane:
        print(järglane)
        tõeväärtus = True
        return tõeväärtus
    else:
        if järglane in sõnastik.keys():
            isa, ema = sõnastik.get(järglane)
            if väljasta_liin(eellane, isa, sõnastik) == True:
                print(järglane)
                tõeväärtus = True
                return tõeväärtus
            if väljasta_liin(eellane, ema, sõnastik) == True:
                print(järglane)
                tõeväärtus = True
                return tõeväärtus
            else:
                tõeväärtus = False
    return tõeväärtus
            
sõnastik =   {'Kalle': ('Teet', 'Maris'),
              'Maris': ('Konstantin', 'Mari'),
              'Rita': ('Teet', 'Maris'),
              'Siim': ('Teet', 'Maris'),
              'Mari': ('Karl', 'Leeni'),
              'Teet': ('Joosep', 'Adele'),
              'Adele': ('Johannes', 'Leida'),
              'Konstantin': ('Viktor', 'Jelena'),
              'Joosep': ('August', 'Emma'),
              'Viktor': ('Nikolai', 'Maria')}
        
