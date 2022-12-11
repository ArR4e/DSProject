def väljasta_liin(eel, järg, sugup):
    if järg not in sugup:
        return False
    elif eel in sugup[järg]:
        print (eel)
        print(järg)
        return True
    elif väljasta_liin(eel, sugup[järg][0], sugup)==True:
        print(järg)
        return True
    elif väljasta_liin(eel, sugup[järg][1], sugup)==True:
        print(järg)
        return True
    else:
        return False
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

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
