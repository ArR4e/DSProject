def väljasta_liin(eel_nimi,järg_nimi,sugup_sõn):
    if eel_nimi or järg_nimi in sugup_sõn.items():
        if järg_nimi in sugup_sõn.keys() or eel_nimi in sugup_sõn.values():
            ...
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