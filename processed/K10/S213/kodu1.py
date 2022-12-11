def erinevad_sümbolid(string):
    
    return set(string)
            
def sümbolite_sagedus(string):
    
    sonastik = {}
    charList = list(string)
    
    for i in range(0, len(charList)):
        if charList[i] not in sonastik:
            sonastik[charList[i]] = charList.count(charList[i])

    return sonastik
            
def grupeeri(string):
    
    taishaalikudChar = list("aeiouõäöü")
    kaashaalikudChar = list("bcdfghjklmnpqrsšzžtvwxy")
    
    sonastik = sümbolite_sagedus(string)
    
    grupeeringSonastik = {}
    
    taishaalikud = set()
    kaashaalikud = set()
    muud = set()
    
    for el in sonastik.keys():
        ennik = (el, sonastik[el])
        if el.lower() in taishaalikudChar:
            taishaalikud.add(ennik)
        elif el.lower() in kaashaalikudChar:
            kaashaalikud.add(ennik)
        else:
            muud.add(ennik)
            
    grupeeringSonastik['Täishäälikud'] = taishaalikud
    grupeeringSonastik['Kaashäälikud'] = kaashaalikud
    grupeeringSonastik['Muud'] = muud
    
    return grupeeringSonastik