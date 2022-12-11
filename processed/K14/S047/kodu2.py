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
ahel = []

def väljasta_liin(vanem, laps, sõnastik):
    global ahel
    
    for el in sõnastik:
        if vanem == laps:
            ahel.append(laps)
            for element in ahel:
                print(element)
            return True
        
        elif vanem in sõnastik[el]:
            ahel.append(vanem)
            return väljasta_liin(el, laps , sõnastik)
    
    return False
    
print(väljasta_liin("Mari", "Adele", sõnastik))






