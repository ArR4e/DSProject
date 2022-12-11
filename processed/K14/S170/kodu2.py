def väljasta_liin(eel, järg, sõnastik):
    if eel in sõnastik and järg in sõnastik:
        print(eel)
        järgmine = sõnastik[eel]
        for m in järg:
            väljasta_liin(järgmine, järg, sõnastik)
    if eel not in sõnastik or järg not in sõnastik:
        return False
    return True


sõnastik = { 'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}



print("Kas siin leidub?", väljasta_liin("Leida", "Kalle", sõnastik))