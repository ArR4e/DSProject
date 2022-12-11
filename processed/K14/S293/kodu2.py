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
  'Viktor': ('Nikolai', 'Maria')
}
def väljasta_liin(eellane, järglane, sõnastik):
    if eellane==järglane:
        print(järglane)
        return True
    if järglane in sõnastik:
        if väljasta_liin(eellane, sõnastik[järglane][0], sõnastik)==True:
            print(järglane)
            return True
        elif väljasta_liin(eellane, sõnastik[järglane][1], sõnastik)==True:
            print(järglane)
            return True
        else:
            return False
    else:
        return False

print("Kas liin leidub?", väljasta_liin("Leida", "Kalle", sõnastik))