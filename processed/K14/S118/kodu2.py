def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        print(eellane)
        return True
    elif järglane not in sugupuu:
        return False
    else:
        for vanem in sugupuu[järglane]:
            if väljasta_liin(eellane, vanem, sugupuu):
                print(järglane)
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

print(väljasta_liin('Leida','Kalle',sõnastik))