def väljasta_liin(eellane, järglane, sõnastik):

 
     
     for laps in sõnastik:
        if järglane == eellane:
           print(eellane)
           return True
         
 
        if eellane in sõnastik[laps]:
            if väljasta_liin(laps, järglane, sõnastik):
               print(eellane)
               return True
 
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

väljasta_liin("Leida", "Kalle", sõnastik)


    
    
    











