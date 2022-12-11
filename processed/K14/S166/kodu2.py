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

def väljasta_liin(eellane,järglane,sõnastik):
    if järglane not in sõnastik:
        return False
    elif eellane==järglane:
        return True
    else:
        väärtus=väljasta_liin(eellane,sõnastik[järglane][0],sõnastik)
        if väärtus:
            print(eellane)
            return True
        väärtus2=väljasta_liin(eellane,sõnastik[järglane][1],sõnastik)
        if väärtus2:
            print(eellane)
            return True
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
