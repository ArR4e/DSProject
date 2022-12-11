def erinevad_sümbolid(sõne):
    hulk = set()
    for el in sõne:
        hulk.add(el)
    return hulk
    
def sümbolite_sagedus(sõne):
    j = []
    d = {}
    for sümbol in sõne:
        j.append(sümbol.strip())
    for sümbol in j:
        d[sümbol] = d.get(sümbol, 0) + 1
    return d

def grupeeri(sõne):
    j = []
    d = {}
    d["täishäälikud"] = set()
    d["kaashäälikud"] = set()
    d["muud"] = set()
    for sümbol in sõne:
        j.append(sümbol.strip())
    for sümbol in j:
        d[sümbol] = d.get(sümbol, 0) + 1
    for v in d:
        if v.lower() in 'aeiouõäöü':
            d["täishäälikud"].add((v,d[v]))
        if v.lower() in 'bdfghjklmnprsšzžtv':
            d["kaashäälikud"].add((v,d[v]))
        if v.lower() in ' !@#$%^&*()_+=-0987654321§,./[]''\|"}{><?;:~`±wqc':
            d["muud"].add((v,d[v]))
    return d