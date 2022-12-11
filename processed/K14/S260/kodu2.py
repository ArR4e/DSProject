def väljasta_liin(eellane,järglane,sõnastik):
    for nimi in sõnastik:
        if eellane == järglane:
            print(eellane)
            return True
        if eellane in sõnastik[nimi]:
            if väljasta_liin(nimi,järglane,sõnastik):
                print(eellane)
                return True
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
  'Viktor': ('Nikolai', 'Maria')}

print(väljasta_liin("Leida","Kalle",sõnastik))