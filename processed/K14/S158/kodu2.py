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

def väljasta_liin(eell, järg, sõnastik) :
    if eell == järg:
        return
    else:
        if järg not in sõnastik:
            return
        else:
            a = sõnastik[järg]
            for i in a:
                print(i)
                return väljasta_liin('Adele', i, sõnastik)

print(väljasta_liin('Adele', 'Kalle', sõnastik))