def väljasta_liin(eel,jarg,sonastik):
    if jarg in sonastik.keys():
        if väljasta_liin(eel,sonastik[jarg][0],sonastik) or väljasta_liin(eel,sonastik[jarg][1],sonastik):
            print(jarg)
            return True
    if jarg == eel:
        print(jarg)
        return True
    else:
        return False

sonastik = {
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