sõnastik={
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

def väljasta_liin(eellane,järglane,sõn):
    try:
        isa=sõn[järglane][0]
        ema=sõn[järglane][1]
        liin=[]
        if isa==eellane:
            liin.append(isa)
            return väljasta_liin(isa,järglane,sõn)
        if ema==eellane:
            liin.append(ema)
            return väljasta_liin(ema,järglane,sõn)
        else:
            
            väljasta_liin(eellane,ema,sõn)
    except:
        return 
        
print(väljasta_liin('Leida', 'Kalle', sõnastik))