def väljasta_liin(eellane, järglane, sugupuu):
    if sugupuu[järglane][0] == eellane or sugupuu[järglane][1] == eellane:
        print(eellane)
        print(järglane)
        return True
    elif sugupuu[järglane][0] not in sugupuu and sugupuu[järglane][1] not in sugupuu:
        return False
    else:
        if väljasta_liin(eellane, sugupuu[järglane][0], sugupuu):
            print(järglane)
            return True
        elif väljasta_liin(eellane, sugupuu[järglane][1], sugupuu):
            print(järglane)
            return True
        
        

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

print("Kas liin leidub?", väljasta_liin("Mari", "Adele", sõnastik))