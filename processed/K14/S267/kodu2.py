sõnastik = {'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == eellane:
        return[järglane]
    if järglane not in sõnastik:
        return False
    else:
        isa = sõnastik[järglane][0]
        ema = sõnastik[järglane][1]
        isaliin = väljasta_liin(eellane, isa, sõnastik)
        if isaliin:
            isaliin.append(järglane)
            return isaliin
        else:
            emaliin = väljasta_liin(eellane, ema, sõnastik)
            if emaliin:
                emaliin.append(järglane)
                return emaliin
            else:
                return False
        

    
print(väljasta_liin("Leida", "Kalle", sõnastik))