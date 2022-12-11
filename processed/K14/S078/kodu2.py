def väljasta_liin(nimi1, nimi2, sonastik):
    if nimi2 == nimi1:
        print(nimi1)
        return True
    elif nimi2 in sonastik:
        isa, ema = sonastik[nimi2][0], sonastik[nimi2][1]
        x = väljasta_liin(nimi1, isa, sonastik) or väljasta_liin(nimi1, ema, sonastik)
        if x != False:
            print(nimi2)
        return x
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
            
            