def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == eellane:
        print(järglane)
        return True
    elif järglane not in sõnastik:
        return False
    else:
        for vanem in sõnastik[järglane]:
            if väljasta_liin(eellane, vanem, sõnastik):
                print(järglane)
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

print("Kas liin leidub?", väljasta_liin('Emma', 'Siim', sõnastik))