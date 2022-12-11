sõnastik = {
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
    if eellane == järglane:
        print(eellane)
        return True
    if järglane in sõnastik.keys():
        for vanem in sõnastik[järglane]:
            if väljasta_liin(eellane, vanem, sõnastik) == True:
                print(järglane)
                return True
        return False
    return False
    
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))