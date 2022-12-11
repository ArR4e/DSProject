def väljasta_liin(eellase_nimi, jarglase_nimi, sonastik):
    if eellase_nimi == jarglase_nimi:
        print(eellase_nimi)
        return True
    else:
        for nimi in sonastik:
            if nimi == jarglase_nimi:
                for num in range(len(sonastik[nimi])):
                    if väljasta_liin(eellase_nimi, sonastik[nimi][num], sonastik):
                        print(nimi)
                        return True
        else:
            return False

print(väljasta_liin('Leida', 'Viktor', {
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
}))