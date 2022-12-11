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

def väljasta(vanem, laps, sugupuu):
    print(vanem)
    muutuv=vanem
    väärtused=[]
    keys=[]
    for v in sugupuu.values():
        väärtused.append(v)
    for k in sugupuu.keys():
        keys.append(k)
    while True:
        if muutuv==laps:
            break
        for el in väärtused:
            if muutuv==el[0] or muutuv==el[1]:
                print(keys[väärtused.index(el)])
                muutuv=keys[väärtused.index(el)]
                if muutuv==laps:
                    break

def väärtus(vanem, laps, sugupuu):
    if laps in sugupuu.keys():
        if vanem in sugupuu[laps]:
            
            return True
        else:
            return bool(väärtus(vanem, sugupuu[laps][0], sugupuu) + väärtus(vanem, sugupuu[laps][1], sugupuu))
    else:
        return False
    
def väljasta_liin(vanem, laps, sugupuu):
    if väärtus(vanem, laps, sugupuu):    
        väljasta(vanem, laps, sugupuu)
    return väärtus(vanem, laps, sugupuu)

print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))
