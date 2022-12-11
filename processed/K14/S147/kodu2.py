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
  'Viktor': ('Nikolai', 'Maria')}
def väljasta_liin(eellane,järglane,sõnastik):
    try:
        if eellane in sõnastik[järglane]:
            print(eellane)
            return True
    except: return False
    for nimi in sõnastik[järglane]:
        if väljasta_liin(eellane,nimi,sõnastik):
            print(nimi)
            return True
    else: return False
print(f"Kas liin leidub? {väljasta_liin('Leida', 'Kalle', sõnastik)}")