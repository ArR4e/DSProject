def väljasta_liin(eellane, järglane, sõnastik):
    for eellased in sõnastik:
        
        if eellane in sõnastik[eellased]:
            nimed.append(eellane)
            eellane = eellased
            
            if eellased == järglane:
                nimed.append(eellased)
                
                for liikmed in nimed:
                    print(liikmed)
                    
            return väljasta_liin(eellane, järglane, sõnastik)
        
    if järglane not in nimed:
         print("EI leidu")

nimed = []

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