liin=[]
def väljasta_liin(eellane,järglane,sugupuu):
    isa,ema=sugupuu[järglane][0],sugupuu[järglane][1]
    try:
        if eellane in sugupuu[järglane]:
            liin.append(eellane)
        else:
            try:
                väljasta_liin(eellane,isa,sugupuu)
            except:
                väljasta_liin(eellane,ema,sugupuu)
        return True
    
    except:
        return False

for nimi in liin:
    print(nimi)
print(väljasta_liin('Leida','Kalle',{
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
}))