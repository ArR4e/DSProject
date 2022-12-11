täishäälikud = 'iüueöõoäa' + 'iüueöõoäa'.upper()
kaashäälikud = 'bcdfghjklmnpqrsšzžtvwxy' + 'bcdfghjklmnpqrsšzžtvwxy'.upper()

def erinevad_sümbolid(sisend):
    return set([x for x in sisend])

def sümbolite_sagedus(sisend):
    väljund = {}
    
    for x in sisend:
        if x in väljund:
            väljund[x] += 1
        else:
            väljund[x] = 1
            
    return väljund

def grupeeri(sisend):
    sümbolid = erinevad_sümbolid(sisend)
    väljund = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    
    for sümbol in sümbolid:
        if sümbol in täishäälikud:
            väljund['Täishäälikud'].add((sümbol, sümbolite_sagedus(sisend)[sümbol]))
        elif sümbol in kaashäälikud:
            väljund['Kaashäälikud'].add((sümbol, sümbolite_sagedus(sisend)[sümbol]))
        else:
            väljund['Muud'].add((sümbol, sümbolite_sagedus(sisend)[sümbol]))
            
    return väljund
