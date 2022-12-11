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
  'Viktor': ('Nikolai', 'Maria') }

def väljasta_liin(eellane,järglane, sõnastik):
    if järglane in sõnastik:
        vanemad = sõnastik[järglane]
    else:
        return False
    for i in [0,1]:
        if vanemad[i] == eellane:
            print(vanemad[i])
            print(järglane)
            return True
        else:
            if väljasta_liin(eellane, vanemad[i], sõnastik):
                print(järglane)
                return True
    return False