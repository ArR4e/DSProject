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

def väljasta_liin(eelane,järglane,sõnastik,olemas_liin = []):
    liin = olemas_liin.copy()
    liin.append(järglane)
    
    #Kontrollime kas leitud
    if eelane == järglane:
        liin.reverse()
        for i in liin:
            print(i)
        return True
    
    #Kontrollime kas vanemad on kirjas
    if järglane not in sõnastik:
        return False
    vanem1, vanem2 = sõnastik[järglane]
    
    #Kontrollime kumbagi liini rekursiivselt
    if väljasta_liin(eelane,vanem1,sõnastik,liin.copy()):
        return True
    if väljasta_liin(eelane,vanem2,sõnastik,liin.copy()):
        return True
    return False



print(väljasta_liin('Leida', 'Kalle', sõnastik))