def erinevad_sümbolid(x):
    return set(x)

def sümbolite_sagedus(x):
    b = list(x)
    c = {}
    for el in b:
        if el in c:
            c[el] = c[el] + 1
        else:
            c[el] = 1
    return c
        
def grupeeri(x):
    taishaalikud = {'a','e','u','i','o',"ü","õ","ä","ö"}
    Kaashaalikud = {'w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','y'}
    a = list(x)
    c = {}
    tais = {}
    kaas = {}
    muu = {}
    y = {}
    d = {}
    for el in a:
        if el in taishaalikud:
            if el in tais:
                tais[el] = tais[el] + 1
            else:
                tais[el] = 1
        elif el in Kaashaalikud:
            if el in kaas:
                kaas[el] = kaas[el] + 1
            else:
                kaas[el] = 1
        else:
            if el in muu:
                muu[el] = muu[el] + 1
            else:
                muu[el] = 1
    d["Täishäälikud"] = set(tais.items())
    d["Kaashäälikud"] =set(kaas.items())
    d["Muud"] = set(muu.items())
    return d
grupeeri("as daw ytr fgd")