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
              'Viktor': ('Nikolai', 'Maria')
            }

def väljasta_liin(eellane, järglane, sõnastik):
    if sõnastik[järglane] != eellane:
        return False
    
    for järglane, eellane in sõnastik.items():
        return väljasta_liin(järglane, eellane, sõnastik)
        
    
            
        
print(väljasta_liin('Leida', 'Kalle', sõnastik))

    
        