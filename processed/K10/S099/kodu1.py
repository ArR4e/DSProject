def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    järjend = list(sõne)
    sõnastik = {}
    for el in järjend:
        sõnastik[el] = järjend.count(el)
    return sõnastik

def grupeeri(sõne):
    järjend = list(sõne)
    täis_hulk = set()
    kaas_hulk = set()
    muud_hulk = set()
    sõnastik = {'Täishäälikud': täis_hulk, 'Kaashäälikud': kaas_hulk, 'Muud': muud_hulk}
    täishäälikud = ('a','e','i','o','u','õ','ä','ö','ü')
    kaashäälikud = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y')
    for el in järjend:
        jär = [el, järjend.count(el)]
        if el.lower() in täishäälikud:
            täis_hulk.add(tuple(jär))
        elif el.lower() in kaashäälikud:
            kaas_hulk.add(tuple(jär))
        else:
            muud_hulk.add(tuple(jär))
    return sõnastik