# 2. Väljasta liin

def väljasta_liin(eellase_nimi, järglase_nimi, sõnastik):
    if eellase_nimi == järglase_nimi:
        print(eellase_nimi)
        return True
    if järglase_nimi in sõnastik:
        for vanem in sõnastik[järglase_nimi]:
            if väljasta_liin(eellase_nimi, vanem, sõnastik):
                print(järglase_nimi)
                return True
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

print("Kas liin leidub?", väljasta_liin("Leida", "Kalle", sõnastik))
#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))