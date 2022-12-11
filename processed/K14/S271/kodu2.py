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

s = {'Urmas': ('Artur', 'Ülle'), 'Artur': ('Meelis', 'Ene'), 'Meelis': ('Siim', 'Niina'), 'Siim': ('Priit', 'Krõõt'), 'Ene': ('Oleg', 'Fatme'), 'Oleg': ('Vello',
'Liidia')}

liin = []

def väljasta_liin(eelane, jarglane, sõnastik):
    if f(eelane, jarglane, sõnastik) != False:
        print(f(eelane, jarglane, sõnastik))
        return True
    else:
        return False
    
def f(eelane, jarglane, sõnastik):
    global liin
    
    if eelane == jarglane:
        return [jarglane]
    
    elif jarglane not in sõnastik:
        return False
    
    else:
        isa, ema = sõnastik[jarglane][0], sõnastik[jarglane][1]
        
        try:
            liin = f(eelane, isa, sõnastik)
            liin.append(jarglane)
            return liin
        
        except:
            try:
                liin = f(eelane, ema, sõnastik)
                liin.append(jarglane)
                return liin
            
            except:
                return False