
def erinevad_sümbolid(a):
    return set(a)

def low(a):
    try:
        return a.lower()
    except:
        return False
    
def sümbolite_sagedus(a):
    c=dict.fromkeys(set(a),0)
    for t in a:
        c[t]+=1
    return c

def grupeeri(a):
    tais={'i', 'ü', 'u', 'e', 'ö', 'õ', 'o', 'ä', 'a'}
    kaas={'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'z', 'z', 't', 'v', 'š', 'ž', 'w', 'c', 'q', 'x', 'y'}
    c=sümbolite_sagedus(a)
    
    b={'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    for e in c.keys():
        if low(e) in tais:
            b['Täishäälikud'].add((e,c[e]))
        elif low(e) in kaas:
            b['Kaashäälikud'].add((e,c[e]))
        else:
            b['Muud'].add((e,c[e]))
    return(b)