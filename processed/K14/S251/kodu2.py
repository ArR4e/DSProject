def väljasta_liin(eellane,järglane,sõnastik):
    
    if järglane == eellane:
        print(eellane)
        return eellane
    
    else:
        
        for i in sõnastik:
            
            if i == järglane:
                
                for j in sõnastik[i]:
                    
                    if väljasta_liin(eellane,j,sõnastik):
                        print(järglane)
                        return True

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

print("Kas liin leidub? " , väljasta_liin('Adele','Teet',sõnastik))