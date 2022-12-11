sugupuu = {
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
def väljasta_liin(enimi, jnimi, sugupuu):
    for järglane, eellane in sugupuu.items():
        if jnimi == järglane:
            isa, ema = eellane
            if enimi == isa or enimi == ema:
                print(enimi)
                print(jnimi)
                return True
            elif väljasta_liin(enimi, isa, sugupuu):
                print(jnimi)
                return True
            elif väljasta_liin(enimi, ema, sugupuu):
                print(jnimi)
                return True
    return False

#print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sugupuu))
#print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sugupuu))