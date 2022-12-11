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

def väljasta_liin(nimi1, nimi2, sõnastik):
    try:
        if nimi1 in sõnastik[nimi2]:
            print(nimi1)
            print(nimi2)
            return True
        else:
            for nimi in sõnastik[nimi2]:
                if väljasta_liin(nimi1, nimi, sõnastik):
                    print(nimi2)
                    return True
            return False
    except:
        return False
