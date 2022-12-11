'''
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
'''
def väljasta_liin(eellane, järglane, sõnastik):
    if järglane in sõnastik.keys():
        if eellane in sõnastik[järglane]:
            print(eellane)
            print(järglane)
            return True
        else:
            kontroll = väljasta_liin(eellane, sõnastik[järglane][0], sõnastik) or väljasta_liin(eellane, sõnastik[järglane][1], sõnastik)
            if kontroll:
                print(järglane)
            return kontroll
    else:
        return False
