def erinevad_sümbolid(sõne):
    return set(sõne)
    

def sümbolite_sagedus(sõne):
    a = erinevad_sümbolid(sõne)
    dict = {}
    for el in a:
        dict[el] = sõne.count(el)
    return dict
        
def grupeeri(sõne):
    dict = {'Täishäälikud': (), 'Kaashäälikud': (), 'Muud': ()}
    sagedused = sümbolite_sagedus(sõne)
    sümbolid = erinevad_sümbolid(sõne)
    täishäälikud = set()
    kaashäälikud = set()
    muud = set()
    for el in sõne:
        if el in set('aeiouöäõü') or el in set('AEIOUÖÄÕÜ'):
            täishäälikud.add((el, sagedused[el]))
        elif el in set('qwrtypsdfghjklzxcvbnm') or el in set('QWRTYPSDFGHJKLZXCVBNM'):
            kaashäälikud.add((el, sagedused[el]))
        else:
            muud.add((el, sagedused[el]))
    dict['Täishäälikud'] = täishäälikud
    dict['Kaashäälikud'] = kaashäälikud
    dict['Muud'] = muud
    return dict
