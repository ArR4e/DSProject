def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sagedus = {}
    for i in erinevad_sümbolid(sõne):
        sagedus[i] = sõne.count(i)
    return sagedus
        
def grupeeri(sõne):
    import string
    sõne.lower()
    grupp = {}
    täis = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
    kaas = []
    muud = 0
    sagedus = sümbolite_sagedus(sõne)
    
    for i in string.ascii_lowercase:
        if i not in täis:
            kaas += [i]
            
    variandid = ['Täishäälikud', 'Kaashäälikud', 'Muud']
    variandi_hulgad = [täis, kaas, muud]
    
    for i in variandid:
        võtmevaartus = set()
        
        try:
            for j in sagedus:
                if j in variandi_hulgad[variandid.index(i)]:
                    ennik = (j, sagedus[j])
                    võtmevaartus.add(ennik)
            grupp[i] = võtmevaartus
            
        except:
            for j in sagedus:
                if j not in täis and j not in kaas:
                    ennik = (j, sagedus[j])
                    võtmevaartus.add(ennik)
            grupp[i] = võtmevaartus
            
    return grupp

print(grupeeri("sõida tasa üle silla"))
        
    

