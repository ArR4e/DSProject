def erinevad_sümbolid(a):
    return set(a)

def sümbolite_sagedus(a):
     sagedus = {}
     for i in a:
         if i in sagedus:
             sagedus[i] += 1
         else:
             sagedus[i] = 1
     return sagedus
täishäälikud = ['a', 'e', 'i', 'o', 'u', 'ü', 'õ', 'ö', 'ä']
ktäishäälikud = täishäälikud + [x.upper() for x in täishäälikud]
print(ktäishäälikud)
def grupeeri(a):
    grupid = {'Täishäälikud': set(),'Kaashäälikud':set(),'Muud':set()}
    b = sümbolite_sagedus(a)
    for symbol, count in b.items():
        if symbol in ktäishäälikud:
            grupid['Täishäälikud'].add((symbol, count))
        elif symbol.isalpha() == True:
            grupid['Kaashäälikud'].add((symbol, count))
        else:
            grupid['Muud'].add((symbol, count))
    return grupid
