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

def väljasta_liin(eellane,järglane,sõnastik):
    for i in sõnastik:
        if järglane in sõnastik :
            print(sõnastik(0,1))
    if järglane in sõnastik:
        print("Kas liin leidub?" + "True")
    if not järglane in sõnastik:
        print("Kas liin leidub?" + "False")
    return väljasta_liin(eellane,järglane,sõnastik)

print("Kas liin leidub?", väljasta_liin("Leida","Kalle", sõnastik))