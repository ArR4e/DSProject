#Teksti analüüs

def erinevad_sümbolid(tekst):
    sümbolid = set()
    
    for tähemärk in tekst:
        if tähemärk not in sümbolid:
            sümbolid.add(tähemärk)
        else:
            continue
    return sümbolid


def sümbolite_sagedus(tekst):
    sagedused = {}
    for tähemärk in tekst:
        sagedused.setdefault(tähemärk, 0)
        sagedused[tähemärk] += 1
    return sagedused


def grupeeri(tekst):
    sagedused = sümbolite_sagedus(tekst)
    grupeeritud =  {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    
    for paar in sagedused.items():
        if paar[0] in {'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü'}:
            grupeeritud['Täishäälikud'].add(paar)
        elif paar[0] in {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 't', 'v', 'w', 'x', 'y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y'}:
            grupeeritud['Kaashäälikud'].add(paar)
        else:
            grupeeritud['Muud'].add(paar)
    return grupeeritud          
    
            
            