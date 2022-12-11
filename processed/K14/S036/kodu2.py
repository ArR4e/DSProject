def väljasta_liin(eelane,järglane,sugupuu):
    if eelane == järglane:
        print(eelane)
        return True
    if järglane not in sugupuu.keys():
        return False
        
    isa,ema = sugupuu[järglane]
    
    is_isa = väljasta_liin(eelane,isa,sugupuu)
    is_ema = väljasta_liin(eelane,ema,sugupuu)
    
    if is_isa or is_ema :
        print(järglane)
        return True
    else:
        return False

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
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle',sõnastik))
        