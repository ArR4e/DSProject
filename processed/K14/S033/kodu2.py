sõnastik = {
    #laps       vanemad
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

def väljasta_liin(vanem, laps, sugupuu):
    if laps == vanem:
        return True
    for i,j in sugupuu.items():
        if vanem in sugupuu[i]:
            vanem = i
            if väljasta_liin(vanem, laps, sugupuu) == True:
                print(vanem)
                return True
    else:
        return False
    
    
print("Kas liin leidub?", väljasta_liin("Mari", "Adele", sõnastik))