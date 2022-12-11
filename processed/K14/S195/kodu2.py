d = {
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

def väljasta_liin(nimi1,nimi2,d):
    if nimi2 == nimi1:
        return True
    else:
        if nimi2 in d:
            väljasta_liin(nimi1,d[nimi2][0],d)
            väljasta_liin(nimi1,d[nimi2][1],d)
            print(nimi2)
    return False
    
        

print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', d))