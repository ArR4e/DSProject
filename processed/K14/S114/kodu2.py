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


def väljasta_liin(eellasenimi,järglasenimi,sugupuu):
    võtmed = list(sugupuu.keys())
    väärtused = list(sugupuu.values())
    
    for i in sugupuu.values():
        if eellasenimi in i:
            JärglaseIndeks = väärtused.index(i)
            print(võtmed[JärglaseIndeks])
            if võtmed[JärglaseIndeks] == järglasenimi:
                return True
            else:
                väljasta_liin(võtmed[JärglaseIndeks],"Kalle",sõnastik)
            if väljasta_liin(võtmed[JärglaseIndeks],järglasenimi,sõnastik) == True:
                return True
            else:
                return False
            

print("Kas liin leidub? ",väljasta_liin("Leida","Kalle",sõnastik))
