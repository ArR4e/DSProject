sõnastik={
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

def väljasta_liin(eellane,järglane,sõnastik,sugupuu=[]):
    if eellane == järglane:
        sugupuu.append(eellane)
        for nimi in sugupuu:
            print(nimi)
    for laps,vanemad in sõnastik.items():
        if eellane in vanemad:
            if eellane not in sugupuu:
                sugupuu.append(eellane)
                väljasta_liin(laps,järglane,sõnastik,sugupuu)
    if järglane in sugupuu:
        return True
    else:
        return False

    
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))



