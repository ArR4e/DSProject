def erinevad_sümbolid(sone):
    hulk = set(sone)
    return hulk

def  sümbolite_sagedus(sone):
    sumbolidSagedusega = {}
    sumbolid = erinevad_sümbolid(sone)
    
    for i in sumbolid:
        sagedus = 0
        
        for j in sone:
            if j == i:
                sagedus += 1
                
        sumbolidSagedusega[i] = sagedus
        
    return sumbolidSagedusega

def grupeeri(sone):
    taishaalikud = 'aeiouõäöü'
    kaashaalikud = 'bcdfghjklmnprsšzžtvqwxy'
    sonastik = {'Täishäälikud': set(), 'Kaashäälikud': set(),'Muud': set() }
    sagedus = sümbolite_sagedus(sone)
    for i in sagedus:
        ennik = (i, sagedus[i])
        if ennik[0].lower() in taishaalikud:
            sonastik['Täishäälikud'].add(ennik)
        elif ennik[0].lower() in kaashaalikud:
            sonastik['Kaashäälikud'].add(ennik)
        else:
            sonastik['Muud'].add(ennik)
            
    return sonastik 