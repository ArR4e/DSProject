def väljasta_liin(eellane, järglane, sugupuu_sõnastik):
    if järglane == eellane:
        print(eellane)
        return True
    elif järglane not in sugupuu_sõnastik:
        return False
    
    vanemad = sugupuu_sõnastik[järglane]
    for vanem in vanemad:
        if vanem.lower() == eellane.lower():
            print(vanem)
            print(järglane)
            return True
    for vanem in vanemad:
        if väljasta_liin(eellane, vanem, sugupuu_sõnastik):
            print(järglane)
            return True
    return False

s = {
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

print(väljasta_liin("Mari", "Adele", s))