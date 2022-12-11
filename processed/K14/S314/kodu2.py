def väljasta_liin(eellane,järglane,sõnastik):
    for laps in sõnastik:
        if eellane in sõnastik[laps]:
            print(eellane)
            if laps == järglane:
                print(järglane)
                return True
            else:                
                if väljasta_liin(laps,järglane,sõnastik) == True:     
                    return True
                else:
                    return False
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
 
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
            