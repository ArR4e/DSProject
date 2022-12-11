def erinevad_sümbolid(s):
    return set([c for c in s])
def sümbolite_sagedus(s):
    d = {}
    for x in set(s):
        d[x]=s.count(x)
    return d
def grupeeri(s):
    th = "aeiouõäöü"
    kh = "qwrtypsdfghjklzxcvbnm"
    d = {"Täishäälikud":set(),"Kaashäälikud":set(),"Muud":set()}
    for x in set([c for c in s]):
        if x in th or x in th.upper():
            d["Täishäälikud"].add((x,s.count(x)))
        elif x in kh or x in kh.upper():
            d["Kaashäälikud"].add((x,s.count(x)))
        else:
            d["Muud"].add((x,s.count(x)))
    return d
            