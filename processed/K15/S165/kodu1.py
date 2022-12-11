import re

def väljasta_kasutaja(fail):
    f = open(fail, "r", encoding = "UTF-8")
    adressid = f.readlines()
    for adress in adressid:
        if re.search("/www\.ut\.ee/", adress):
            kasutaja = re.search("/~([A-Za-z0-9]*)/", adress)
            if kasutaja:
               print(kasutaja.group()[2:-1])
    f.close()


väljasta_kasutaja("aadressid.txt")
                
                
        
    
    
    
    
    

        
    

    
            
        
        

        







    
    
    




      
   
   
   
   