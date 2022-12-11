def väljasta_liin(vanem, laps, sõnastik):
    if vanem == laps:
        print(laps)
        return [laps]
    elif laps not in sõnastik:
        return False
    else:
        isa, ema = sõnastik[laps][0], sõnastik[laps][1]
        isa_liin = väljasta_liin(vanem, isa, sõnastik)
        if isa_liin:
            print(laps)
            return True
        else:
            ema_liin = väljasta_liin(vanem, ema, sõnastik)
            if ema_liin:
                print(laps)
                return True
            else:
                return False
                
    
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