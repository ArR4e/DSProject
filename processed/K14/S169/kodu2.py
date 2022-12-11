sõnastik= {
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

def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == eellane:
        print(eellane)
        return True
    if järglane in sõnastik:
        for isavema in sõnastik[järglane]:
            if väljasta_liin(eellane, isavema, sõnastik) == True:
                print(järglane)
                return True
    return False
              
print(väljasta_liin("Leida","Kalle",sõnastik))