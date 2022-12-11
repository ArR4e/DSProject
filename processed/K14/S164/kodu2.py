liin = []
def väljasta_liin(eellase_nimi, järglase_nimi, sõnastik):
    liin.append(eellase_nimi)
    if järglase_nimi in sõnastik:
        for nimi in sõnastik:
            if sõnastik[nimi][0] == eellase_nimi or sõnastik[nimi][1] == eellase_nimi:
                if nimi == järglase_nimi:
                    liin.append(nimi)
                    for liini_nimi in liin:
                        print(liini_nimi)
                    return True
                else:
                    return väljasta_liin(nimi, järglase_nimi, sõnastik) 
    else:
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


print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))