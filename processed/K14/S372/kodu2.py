def väljasta_liin(eellane, järglane, sõnastik):
    for laps, vanemad in sõnastik.items():
        isa, ema = vanemad
        if ema == eellane or isa == eellane:
            nende_laps = laps
            print(eellane)
            for laps, vanemad in sõnastik.items():
                ema, isa = vanemad
                if nende_laps == isa or nende_laps == ema:
                    nende_lapse_laps = laps
                    if eellane != järglane:
                        väljasta_liin(nende_laps, nende_lapse_laps, sõnastik)            
        
    
    
    
    
    
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
print(väljasta_liin("Leida", "Kalle", sõnastik))
