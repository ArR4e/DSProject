rida = []

def väljasta_liin(eellane, järglane, sõnastik):
    print(eellane)
    for võti, vanemad in sõnastik.items():
        if eellane==järglane:
            break
        elif eellane in vanemad[0]:
            ellane=võti
            väljasta_liin(eellane, järglane, sõnastik)
        elif eellane in vanemad[1]:
            eellane= võti
            väljasta_liin(eellane, järglane, sõnastik)
    isa, ema = sõnastik[järglane][0], sõnastik[järglane][1]
    
    try:
        if eellane in d[järglane]:
            rida.append(eellane)
        else:
            try:
                väljasta_liin(eellane, isa, sõnastik)
            except:
                väljasta_liin(eellane, ema, sõnastik)
        
        return True
    
    except:
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
print("Kas liin leidub?", väljasta_liin('Leida','Kalle', sõnastik))
    
    