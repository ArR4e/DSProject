

def erinevad_sümbolid(sõne):
    sõne = set(sõne)
    
    return sõne

def sümbolite_sagedus(sõne):
    hulk = {}
    for el in sõne:
        hulk[el] = hulk.get(el, 0) + 1
       
    return hulk  
    
def grupeeri(sõne):
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    
    häälikud = sümbolite_sagedus(sõne)


    for key in häälikud.items():
        y = key[0]
        if y.lower() in 'aeiouüõöä':
            sõnastik['Täishäälikud'].add(key)
        if y.lower() in 'sdgfhzxcwqyklyvbnjmrtp':
            sõnastik['Kaashäälikud'].add(key)
        if y.lower() in ' " ?!+-,.':
            sõnastik['Muud'].add(key)
    
    for hulk in sõnastik:
        return sõnastik
        
     
        
        
        