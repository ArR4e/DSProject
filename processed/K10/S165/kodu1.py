def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk


def sümbolite_sagedus(sõne):
    sümbolid = list(sõne)
    d = {}
    for el in sümbolid:
        d[el] = d.get(el, 0) + 1
    return d

def grupeeri(sõne):
    sümbolid = sümbolite_sagedus(sõne)
    sümbolid_listina = []
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    kaashäälikud = "bdfghjklmnpršszžtvqywxcBDFGHJKLMNPRSZŠŽTVQXCYW" 
    täishäälikute_hulk = set()
    kaashäälikute_hulk = set()
    muu_hulk = set()
    d = {}
       
    
    for el in sümbolid:
        k = (el, sümbolid[el])
        sümbolid_listina.append(k)
        
    for el in sümbolid_listina:
        if el[0] in täishäälikud:
            täishäälikute_hulk.add(el)  
        elif el[0] in kaashäälikud:
            kaashäälikute_hulk.add(el)     
        else:
            muu_hulk.add(el)
            
    d["Täishäälikud"] = täishäälikute_hulk
    d["Kaashäälikud"] = kaashäälikute_hulk
    d["Muud"] = muu_hulk
    
    return d




        
    

    
            
        
        

        







    
    
    




      
   
   
   
   