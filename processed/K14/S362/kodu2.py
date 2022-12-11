
def väljasta_liin(eellase_nimi, järglase_nimi,sugupuu_sõnastik):
   
   for el in sugupuu_sõnastik:
       if eellase_nimi in sugupuu_sõnastik[el]:
            print(eellase_nimi)
            väljasta_liin(el, järglase_nimi,sugupuu_sõnastik)
            
           
            
            if el==järglase_nimi:
                print(järglase_nimi)
                break
            return True
   return False
            
          
                #return True
               
        
            

#             if el!= järglase_nimi or el not in sugupuu_sõnastik.values():
#                     return "Kas liin leidub?", False
                                    
                
#         else:
#            print("Kas liin leidub?", False)
    
    
                
#         if eellase_nimi not in sugupuu_sõnastik[el]:
#                     return False
        
            
    
    #väljasta_liin(el, järglase_nimi,sugupuu_sõnastik)
    
            
            #print(el)
            #continue
            #väljasta_liin(el, järglase_nimi,sugupuu_sõnastik)
        

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
  'Viktor': ('Nikolai', 'Maria')}
# for el in sõnastik:
#     if eellase_nimi in sugupuu_sõnastik[el] or eellase_nimi==el:
#         if järglase_nimi in sugupuu_sõnastik.values() or eellase_nimi in sugupuu_sõnastik.keys():
#             print(True)
#             
#               

print("Kas liin leidub?", väljasta_liin('Jürgen', 'Kaja',sõnastik))
