
def erinevad_sümbolid(sõne):
    hulk = set()
    for element in sõne:
        hulk.add(element)
    return hulk
               
# print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for sümbol in sõne:
        if sümbol in sõnastik:
            sõnastik[sümbol] += 1
        else:
            sõnastik[sümbol] = 1
    return sõnastik

#print(sümbolite_sagedus("Hei hopsti, Väikevend!"))
def grupeeri(sõne):
    täishäälikud = {'a', 'e', 'i', 'o', 'u', 'õ','ä', 'ö','ü'}
    kaashäälikud = {'c', 'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž' , 't', 'v', 'w', 'q', 'x', 'y'}
    sõnastik = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    sümbolite_sagedused = sümbolite_sagedus(sõne)

    for sümbol in sõne:
        if sümbol.lower() in täishäälikud:
            sõnastik['Täishäälikud'].add((sümbol, sümbolite_sagedused[sümbol]))
        elif sümbol.lower() in kaashäälikud:
            sõnastik['Kaashäälikud'].add((sümbol, sümbolite_sagedused[sümbol]))
        else:
            sõnastik['Muud'].add((sümbol, sümbolite_sagedused[sümbol]))
        
    return sõnastik

    
    
    
    
    
    
    