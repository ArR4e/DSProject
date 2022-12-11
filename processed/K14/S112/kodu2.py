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

def väljasta_liin(eellane,järglane,sõnastik):
    
    if järglane in sõnastik:
        for i in sõnastik[järglane]:
            if i == eellane:
                print(i)
                print(järglane)
                return True
            elif i in sõnastik:
                if väljasta_liin(eellane,i,sõnastik) == True:
                    print(järglane)
                    return True
    return False

            
print('Kas liin leidub?', väljasta_liin('Leida','Kalle',sõnastik))