
sõnastik={
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

def väljasta_liin(eellane, järglane, sõnastik):
    try:
        print(eellane)
        for võti in sõnastik:
            if eellane in sõnastik[võti]:
                if järglane == võti:
                    print(järglane)
                    return True
                if järglane != võti:
                    väljasta_liin(võti, järglane, sõnastik)
                    if järglane in sõnastik[võti]:
                        return True
                    else:
                        return False
    except:
        return False
print("Kas leidub liin?", väljasta_liin("August", "Maris", sõnastik))
        
    
