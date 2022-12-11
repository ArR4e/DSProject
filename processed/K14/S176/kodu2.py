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

def väljasta_liin(eellane, järglane, sõnastik):
    if eellane == järglane:
        print(järglane)
        return[järglane]
    elif järglane not in sõnastik:
        return False
    else:
        isa, ema = sõnastik[järglane][0], sõnastik[järglane][1]
        
        liin = väljasta_liin(eellane, isa, sõnastik) or väljasta_liin(eellane, ema, sõnastik)
        if liin:
            print(järglane)
            return True
        else:
            return False



