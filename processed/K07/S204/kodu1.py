
järjend=['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']



def poisse_ja_tüdrukuid(järjend):
    p=0
    t=0
    
    for n in järjend:
        uus_järjend = n.split(' ')
        
        if uus_järjend[-1] == "P":
            p+=1
        if uus_järjend[-1] == "T":
            t+=1
    
    
    return(p, t)
    
            
   
        

print(poisse_ja_tüdrukuid(järjend))


