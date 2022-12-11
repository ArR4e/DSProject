def väljasta_liin(eellane, jarglane, sonastik):
    try:
        if eellane == sonastik.get(jarglane)[0] or eellane == sonastik.get(jarglane)[1]:
            print(eellane)
            print(jarglane)
            return True
        if väljasta_liin(eellane, sonastik[jarglane][0], sonastik):
            print(jarglane)
            return True
        if väljasta_liin(eellane, sonastik[jarglane][1], sonastik):
            print(jarglane)
            return True
        return False
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

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))