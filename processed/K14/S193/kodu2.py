def väljasta_liin(e_nime, j_nime, s):
    if e_nime == j_nime:
        print(e_nime)
        return True
  
    if j_nime in s:
        isa_nim = s[j_nime]
        ema_nim = s[j_nime]
        tõeväärtus = väljasta_liin(e_nime, isa_nim, s)
        tõeväärtus = väljasta_liin(e_nime, ema_nim, s)
        if tõeväärtus:
            print(j_nime)
        return tõeväärtus
    
    else:
        return False
    
    

s = {'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', s))