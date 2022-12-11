def väljasta_liin(ell,jar,puu):
    if help(ell,jar,puu) == True:
        for el in puu.values():
            if ell in el:
                print(ell)
                if ell in puu[jar]:
                    print(jar)
                    return True
                for i in puu:
                    if puu[i] == el:
                        return väljasta_liin(i,jar,puu)
    return False
def help(ell,jar,puu):
    for el in puu.values():
            if ell in el:
                if ell in puu[jar]:
                    return True
                for i in puu:
                    if puu[i] == el:
                        return help(i,jar,puu)
        
                
                

    
    
puu = {
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

print(väljasta_liin('Mari', 'Adele',puu))
