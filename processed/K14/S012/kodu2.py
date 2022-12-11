#nädal 14, kodu2

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
            print(järglane)
            return True
        elif True:
            for laps in sõnastik:
                if eellane in sõnastik[laps]:
                    print(eellane)
                    eellane = laps
                    return väljasta_liin(eellane, järglane, sõnastik)
        else:
            return False
        


        
väljasta_liin('Leida', 'Kalle', sõnastik)

    