liin = []
def väljasta_liin(eellane, järglane, sugupuu):
    for el in sugupuu:
        if eellane in sugupuu[el]:
            liin.append(eellane)
            if el != järglane:
                return(väljasta_liin(el, järglane, sugupuu))
            else:
                liin.append(järglane)
                for el in liin:
                    print(el)
                return True
    return False

sonastik = {
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
print("Kas liin leidub?", väljasta_liin('Leida','Kalle',sonastik))