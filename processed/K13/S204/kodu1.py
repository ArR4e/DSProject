def auto_hind(hind, aastad):
    
    #def baas(aastad):
    if aastad < 1:
        return round(hind, 2)
    #return baas(aastad)   
        
    
    
    #def samm(hind, aastad):
        #while aastad >= 1:
        
    else:
        uus_hind = hind * (1-(20/100))
        uued_aastad = aastad - 1
            
            #aastad-=1
        return auto_hind(uus_hind, uued_aastad)
    #return samm(hind, 5)
    
    
#print(auto_hind(10000.0, 8))