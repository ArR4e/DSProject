def väljasta_liin(eel, jär, sõnastik, t=[]):
    if jär in sõnastik[eel][0] or jär in sõnastik[eel][1]:
        t.append(eel)
        t.append(jär)
        #t.append(väljasta_liin(jär, eel, sõnastik, []))
        return True
    else:
        for el in sõnastik:
            if jär in sõnastik[el][0] or jär in sõnastik[el][1]:
                leidub=väljasta_liin(eel, el, sõnastik, [])
            #t.append(eel)
            #t.append(jär)
                t.append(väljasta_liin(eel, el, sõnastik, []))
                if leidub:
                    return True
        return False
    return t
        
    
#print(väljasta_liin('Joosep', 'Kalle',
{
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