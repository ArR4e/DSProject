def suguluse_tuvastamine(eellane, järglane, sõnastik):
    järjend = []
    if eellane == järglane:
        järjend.append(eellane)
        return ""
    elif järglane not in sõnastik:
        return False
    else:
        try:
            isa = sõnastik[järglane][0]
            ema = sõnastik[järglane][1]
            return isa + ", " + suguluse_tuvastamine(eellane, isa, sõnastik)
        except:
            try:
                return ema + ", " + suguluse_tuvastamine(eellane, ema, sõnastik)
            except:
                return False
             
def väljasta_liin(eellane, järglane, sõnastik):
    sugulus = suguluse_tuvastamine(eellane, järglane, sõnastik)
    if sugulus == False:
        return False
    else:
        järjend = list(sugulus.split(", "))
        for el in järjend[::-1]:
            print(el)
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
  'Viktor': ('Nikolai', 'Maria')
}

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))