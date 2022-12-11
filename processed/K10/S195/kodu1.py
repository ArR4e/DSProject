def erinevad_sümbolid(x):
    y = set()
    for el in x:
        y.add(el)
    return y

def sümbolite_sagedus(x):
    hulk = set()
    jark = []
    d = {}
    for el in x:
        hulk.add(el)
        jark.append(el)
    for el in hulk:
        d[el] = jark.count(el)
    return d

def grupeeri(x):
    taishaalik = ['a', 'e', 'i', 'o', 'u', 'ö', 'ä', 'ü', 'õ']
    kaashaalik = ['q', 'c', 'j', 'l', 'm', 'n', 'r', 'v', 'k', 'p', 't', 'g', 'b', 'd', 'f', 'h', 's', 'z']
    taisjark = []
    kaasjark = []
    muujark = []
    hulk = set()
    jark = []
    dic = {}
    for el in x:
        hulk.add(el)
        jark.append(el)
    for el in hulk:
        if el in taishaalik:
            taisjark.append([el,jark.count(el)])
        elif el in kaashaalik:
            kaasjark.append([el,jark.count(el)])
        else:
            muujark.append([el,jark.count(el)])
    dic["Täishäälikud"] = taisjark
    dic["Kaashäälikud"] = kaasjark
    dic["Muud"] = muujark
    return dic
    
    
    