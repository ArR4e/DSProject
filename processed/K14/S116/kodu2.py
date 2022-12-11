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
    
    else:
        for laps in sõnastik:
            if laps == järglane:
                for vanem in sõnastik[laps]:
                    if väljasta_liin(eellane, vanem, sõnastik):
                        print(järglane)
                        return True
        
print("Kas liin leidub?", väljasta_liin('Leida', 'Teet', sõnastik))
        
    