sõnastik = {
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria'),
  'Kalle': ('Teet', 'Maris')
}

def väljasta_liin(eellane, järglane, sõnastik, ahel = [], stop = 0):
    if järglane == eellane:
        ahel.append(eellane)
        return True
    else:
        for key in sõnastik.keys():
            if eellane in sõnastik[key]:
                if väljasta_liin(key, järglane, sõnastik, stop = stop + 1) == True:
                    ahel.append(eellane)
                    if stop == 0:
                        for osa in reversed(ahel):
                            print(osa)
                    return True
                    
    return False

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))