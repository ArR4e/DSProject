def väljasta_liin(enimi, jnimi, s):
    if enimi == jnimi:
        print(enimi)
        return True
    for i in (0, 1):
        try:
            if väljasta_liin(enimi, s[jnimi][i], s):
                print(jnimi)
                return True
        except: pass
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