rel = {
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

def väljasta_liin(eellane, järglane, sõnastik):
    if järglane in sõnastik:
        if eellane in sõnastik[järglane]:
            print(eellane)
            print(järglane)
            return True
        else:
            for nimi in sõnastik[järglane]:
                if väljasta_liin(eellane, nimi, sõnastik) == True:
                    print(järglane)
                    return True
            return False
    return False

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', rel))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', rel))