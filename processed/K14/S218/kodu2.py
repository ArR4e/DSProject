
def väljasta_liin(eellane, järglane, sugupuu):
    def kontroll(eellane, järglane, sugupuu):
    
    
    

        if eellane == järglane:
            return True 

        

        
        else:
            
            for elem in sugupuu:
                if eellane in sugupuu[elem]:
                    for vanem in sugupuu[elem]:
                        if vanem == eellane:

                                return kontroll(elem, järglane, sugupuu)

    x = kontroll(eellane, järglane, sugupuu)
    if x == True:
        print(eellane)
        for elem in sugupuu:
                if eellane in sugupuu[elem]:
                    for vanem in sugupuu[elem]:
                        if vanem == eellane:
                            väljasta_liin(elem, järglane, sugupuu)
        return True
    else:
        return False
        
    
    
    
    
    
sõnastik ={
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}

print("Kas liin leidub?", väljasta_liin('Leida', 'Adele', sõnastik))   