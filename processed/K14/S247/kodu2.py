def väljasta_liin(eel_nimi, järg_nimi, sõnastik):
    for järglane, eellane in sõnastik.items():
        if järg_nimi == järglane:
            isa, ema = eellane
            if eel_nimi == isa or eel_nimi == ema:
                print(eel_nimi)
                print(järg_nimi)
                return True
            elif väljasta_liin(eel_nimi, isa, sõnastik):
                print(järg_nimi)
                return True
            elif väljasta_liin(eel_nimi, ema, sõnastik):
                print(järg_nimi)
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
  'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
