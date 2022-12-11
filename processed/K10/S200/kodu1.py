def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk



def sümbolite_sagedus(sõne):
    sagedus = {}
    for el in sõne:
        kokku = sõne.count(el)
        sagedus[el]= kokku
    return sagedus

def grupeeri(sõne):
    täishäälikud = ['a','A','e','E','i','I','o','O','u','U','õ','Õ','ä','Ä','ö','Ö','Ü','ü']
    kaashäälikud = ['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','r','R','s','S','š','Š','z','Z','ž','Ž','t','T','v','V','w','W','x','X','y','Y','q','Q']
    grupeeritud = {}
    grupeeritud["Täishäälikud"] = set()
    grupeeritud["Kaashäälikud"] = set()
    grupeeritud["Muud"] = set()
    sagedus = sümbolite_sagedus(sõne)
    
    for võti in sagedus:
        element = str(võti)
        
        if element in täishäälikud:
            kokku = sõne.count(element)
            grupeeritud["Täishäälikud"].add((element,kokku))
        
        elif element in kaashäälikud:
            kokku = sõne.count(element)
            grupeeritud["Kaashäälikud"].add((element,kokku))
        
        else:
            kokku = sõne.count(element)
            grupeeritud["Muud"].add((element,kokku))
            
    
    return grupeeritud


    