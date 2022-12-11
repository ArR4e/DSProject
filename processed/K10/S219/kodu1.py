def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        if sümbol in d:
            d[sümbol] = d[sümbol] + 1
        else:
            d[sümbol] = 1
    return d
    
def grupeeri(sõne):
    d = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    täishäälikud = set("AaEeIiOoUuÕõÄäÖöÜü")
    kaashäälikud = set("BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy")
    
    for sümbol in sõne:
        if sümbol in täishäälikud:
            sümbol_loendur = sõne.count(sümbol)
            d['Täishäälikud'].add((sümbol, sümbol_loendur))
            
        elif sümbol in kaashäälikud:
            sümbol_loendur = sõne.count(sümbol)
            d['Kaashäälikud'].add((sümbol, sümbol_loendur))
            
        else:
            sümbol_loendur = sõne.count(sümbol)
            d['Muud'].add((sümbol, sümbol_loendur))

    return d