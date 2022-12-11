def väljasta_liin(eellase_nimi, jarglase_nimi, sõnastik):
    if eellase_nimi == jarglase_nimi:
        print(eellase_nimi)
        return True
    else:
        for nimi in sõnastik:
            if nimi == jarglase_nimi:
                for num in range(len(sõnastik[nimi])):
                    if väljasta_liin(eellase_nimi, sõnastik[nimi][num], sõnastik):
                        print(nimi)
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

print(väljasta_liin("Leida", "Viktor", sõnastik))