def väljasta_liin(eellane, jarglane, sugupuu):
    v = False
    
    if eellane == jarglane:
        print(jarglane)
        return True
    if not jarglane in sugupuu:
        return False

    v = väljasta_liin(eellane, sugupuu[jarglane][0], sugupuu)
    if v:
        print(jarglane)
        return v
    else:
        v = väljasta_liin(eellane, sugupuu[jarglane][1], sugupuu)
        if v:
            print(jarglane)
            return v
        return v
        
sonastik = {
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

#print("Kas liin leidub? ", valjasta_liin('Leida', 'Kalle', sonastik))