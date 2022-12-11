def väljasta_liin(eellane, järglane, puu):
    if eellane == järglane:
        print(järglane)
        return True
    else:
        for nimi in slovar:
            if järglane in slovar[nimi]:
                print(järglane)
                return True
            break
        return False

print(väljasta_liin('Leida', 'Kalle', slovar)
      
slovar = {
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