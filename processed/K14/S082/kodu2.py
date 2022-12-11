def väljasta_liin(eellane, järglane, sugupuu):
    kas = False
    for a in sugupuu:
        if järglane == a:
            väljasta_liin(eellane, sugupuu.get(a)[0], sugupuu)
            väljasta_liin(eellane, sugupuu.get(a)[1], sugupuu)
            print(järglane)
            
        else:
            if eellane == sugupuu.get(a)[0] or eellane == sugupuu.get(a)[1]:
                print(eellane)
                return True
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
print('Kas liin leidub?', väljasta_liin('Leida', 'Kalle', sugupuu))