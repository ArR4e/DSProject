def väljasta_liin(eellane, järglane, sõnastik, liin):
    if järglane == eellane:
        liin.append(järglane)
        for el in liin:
            print(el)
        return True
    else:
        for laps in sõnastik:
                if eellane in sõnastik[laps]:
                    liin.append(eellane)
                    eellane = laps
                    return väljasta_liin(eellane, järglane, sõnastik, liin)
    if järglane not in liin:
        return False
            
    
   #laps     #isa    #ema
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
liin = []
                                      #eellane #järglane
print('Kas liin leidub?', väljasta_liin('Leida', 'Kalle', sõnastik, liin))