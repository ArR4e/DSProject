def väljasta_liin(vanem, laps, puu):
    if vanem in puu[laps]:
        return print(laps)
    else:
        for el in puu[laps]:
            try:
                return print(väljasta_liin(laps, vanem, puu))
            except:
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

print('Kas siin leidub?', väljasta_liin('Leida', 'Kalle', sõnastik))