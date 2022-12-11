sugupuu={'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

def väljasta_liin(eel, järg, sugupuu):
    if järg not in sugupuu:
        return False
    else:
        for järg in sugupuu.keys():
            if järg[0] == eel:
                print(eel)
                print(järg)
                return True
            elif järg[1] == eel:
                print(eel)
                print(järg)
                return True
            else:
                väljasta_liin(eel[0], järg, sugupuu)
                väljasta_liin(eel[1], järg, sugupuu)
    
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sugupuu))