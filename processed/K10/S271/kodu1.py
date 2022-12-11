def erinevad_sümbolid(sone):
    hulk = set()
    for symbol in sone:
        hulk.add(symbol)
    return hulk

def sümbolite_sagedus(sone):
    Mydict = {}
    sagedus = 0
    for symbol in sone:
        if symbol not in Mydict:
            Mydict[symbol] = 1
        else:
            Mydict[symbol] = Mydict[symbol] + 1
    return Mydict

def grupeeri(sone):
    muud = ''
    tais1 = ''
    kaas1 = ''
    tais = ['a','e','i','o','u','ä','ü','õ','ö','A','E','I','O','U','Ä','Ü','Ö','Õ']
    kaas = ['B','b', 'C','c', 'D','d', 'F','f', 'G','g', 'H','h', 'J','j', 'K','k', 'L','l', 'M','m', 'N','n', 'P','p', 'Q','q', 'R','r', 'S','s', 'Š','š', 'Z','z', 'Ž','ž', 'T','t', 'V','v', 'W','w', 'X','x', 'Y','y']
    
    for symbol in sone:
        if symbol in tais:
            tais1 += symbol
        elif symbol in kaas:
            kaas1 += symbol
        else:
            muud += symbol
    tais2 = set(list(sümbolite_sagedus(tais1).items()))
    kaas2 = set(list(sümbolite_sagedus(kaas1).items()))
    muud2 = set(list(sümbolite_sagedus(muud).items()))
    Mydict = {'Täishäälikud':tais2
                  , 'Kaashäälikud':kaas2
                  , 'Muud':muud2
                }
    return Mydict