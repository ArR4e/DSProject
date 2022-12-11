def väljasta_liin(vanem, laps, dic):
    if vanem == laps:
        print(laps)
        return True
    
    if laps in dic:
        if väljasta_liin(vanem, dic[laps][0], dic) or väljasta_liin(vanem, dic[laps][1], dic):
            print(laps)
            return True
        else:
            return False
    else:
        return False
    
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

väljasta_liin('Leida', 'Kalle', sõnastik)