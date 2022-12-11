
def väljasta_liin(eellane, järglane, sugupuu):
    rek=False
    
    if eellane == järglane:
        liin.append(järglane)
        return True
        
    else:
        for key in sugupuu.keys():
            
            if sugupuu[key][0]==eellane:
                liin.append(sugupuu[key][0])
                rek=väljasta_liin(key, järglane, sugupuu)
                
                if rek==True:
                    for i in range(len(liin)):
                        if liin[i]!=liin[i-1]:
                            print(liin[i])
                    break
                
            elif sugupuu[key][1]==eellane:
                liin.append(sugupuu[key][1])
                rek=väljasta_liin(key, järglane, sugupuu)
                
                if rek==True:
                    
                    break
    
    return rek
 
 
 
 
sõnastik={
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
liin=[]

print("Kas liin leidub?", väljasta_liin('Jelena', 'Kalle', sõnastik))



