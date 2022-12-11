# asi jäi pooleli ,hetkeline lahendus pole päris õige.

def väljasta_liin (eellane, järglane, sõnastik):
    #eellased=[]
    print(eellane)
    for järglane2, eellane2 in sõnastik.items():
        if eellane in eellane2:
            #print(eellane)
            väljasta_liin (järglane2, eellane, sõnastik)
            #eellased.append(eellane)
#     return eellased
            

sõnastik= {
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

v= väljasta_liin('Leida', 'Kalle', sõnastik)