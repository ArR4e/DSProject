sõnastik={
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

def väljasta_liin(eel,järg,sõnastik):
    kontroll=0
    for i in sõnastik:
        if eel in sõnastik[i]:
            if i==järg:
                print(i)
                print(eel)
                kontroll+=1
                return True
            else:
                if väljasta_liin(i,järg,sõnastik):
                    print(eel)
                    kontroll+=1
                    return True
    if kontroll==0:
        return False
väljasta_liin('Leida', 'Kalle', sõnastik)