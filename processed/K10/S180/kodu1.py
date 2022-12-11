def erinevad_sümbolid(sõne):
    sõne = set(sõne)
    return sõne

def sümbolite_sagedus(sõne):
    global loe
    loe = {}
    for täht in sõne:
        if täht.lower() in loe:
            loe[täht] = loe[täht] + 1
        else:
            loe[täht] = 1
    return loe
        
def grupeeri(sõne):
    
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    täishäälikud['Täishäälikud'] = set()
    kaashäälikud['Kaashäälikud'] = set()
    muud['Muud'] = set()
    
    sümbolite_sagedus(sõne)
    
    for täht in loe:
        if täht.lower() in set('aeiouõäöü'):
            täishäälikud['Täishäälikud'].add((täht, loe[täht]))
        elif täht.lower() in set('kptgbdhjlmnrvscfšzžxyqw'):
            kaashäälikud['Kaashäälikud'].add((täht, loe[täht]))
        else:
            muud['Muud'].add((täht, loe[täht]))
            
    kokku = {**täishäälikud, **kaashäälikud, **muud}
    return kokku