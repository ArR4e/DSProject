def väljasta_liin(eel, järg, sõnastik):
    if eel == järg:
        print(eel)
        return True
    if järg in sõnastik:
        i = sõnastik[järg][0]
        j = sõnastik[järg][1]
        tõeväärtus = väljasta_liin(eel, i, sõnastik) or väljasta_liin(eel, j, sõnastik)
        if tõeväärtus:
            print(järg)
        return tõeväärtus
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
