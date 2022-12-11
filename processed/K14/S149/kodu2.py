def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(eellane)
        return True
    elif järglane not in sõnastik:
        return False
    elif väljasta_liin(eellane, sõnastik[järglane][0], sõnastik) == True or väljasta_liin(eellane, sõnastik[järglane][1], sõnastik) == True:
        print(järglane)
        return True
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
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))