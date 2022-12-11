def väljasta_liin(eellase_nimi, järglase_nimi, sõnastik):
    if järglase_nimi in sõnastik:
        if eellase_nimi in sõnastik[järglase_nimi]:
            print(eellase_nimi)
            print(järglase_nimi)
            return True
        for i in sõnastik[järglase_nimi]:
            if väljasta_liin(eellase_nimi, i, sõnastik):
                print(järglase_nimi)
                return True   
    return False
sugupuu = {
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
