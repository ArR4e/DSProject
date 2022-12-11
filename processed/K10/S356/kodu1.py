def erinevad_sümbolid(a):
    erinevad = set()
    for i in a:
        if i not in erinevad:
            erinevad.add(i)
    return erinevad

def sümbolite_sagedus(a):
    sagedus = {}
    for i in a:
        if i not in sagedus:
            sagedus[i] = 1
        else:
            sagedus[i] += 1
    return sagedus

def grupeeri(a):
    
    tais = set()
    kaas = set()
    muud = set()
    repeat = set()
    grupp = {'Täishäälikud' : '', 'Kaashäälikud' : '', 'Muud' : ''}
    th = ['A','a','E','e','I','i','O','o','U','u','Ü','ü','Õ','õ','Ö','ö','Ä','ä']
    kh = ['b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
                 
    for i in a:
        nr = a.count(i)
        if i not in repeat:
            repeat.add((i, nr))
    
    for i in repeat:
        if i[0] in th:
            tais.add(i)
        elif i[0] in kh:
            kaas.add(i)
        else:
            muud.add(i)
            
    grupp['Täishäälikud'] = tais
    grupp['Kaashäälikud'] = kaas
    grupp['Muud'] = muud
    return grupp