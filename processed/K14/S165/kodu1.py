def rek_abs(järjend):
    uus_list = []
    for el in järjend:
        if isinstance(el, list):
            uus_list.append(rek_abs(el))
            
        else:
            uus_list.append(abs(el))
            
    return uus_list
    
    
print(rek_abs([]))
    
    
    
    
    

        
    

    
            
        
        

        







    
    
    




      
   
   
   
   