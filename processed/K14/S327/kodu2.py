liin = []
def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == "Ülle":
        return False
    liin.append(eellane)
    for el in sõnastik:
        if eellane in sõnastik[järglane]:
            liin.append(järglane)
            a = []
            for el in liin:
                if el not in a:
                    a.append(el)
            for el in a:
                print(el)
            return True
        else:
            if eellane in sõnastik[el]:
                if el not in liin:
                    liin.append(el)
                return väljasta_liin(el, järglane, sõnastik)
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
print(väljasta_liin("Leida", "Kalle", sõnastik))