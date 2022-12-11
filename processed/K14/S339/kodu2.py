def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        print(järglane)
        return True
    if järglane in sugupuu:
        isa = sugupuu[järglane][0]
        ema = sugupuu[järglane][1]
        eellane_leidub = väljasta_liin(eellane, isa, sugupuu) or väljasta_liin(eellane, ema, sugupuu)
        if eellane_leidub:
            print(järglane)
        return eellane_leidub
    else:
        return False


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

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sugupuu))