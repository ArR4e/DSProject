def erinevad_sümbolid(a):
    hulk = set(str(a))
    return hulk
def sümbolite_sagedus(b):
    jär = list(b)
    d = {}
    for arv in jär:
        if arv in d:
            d[arv] = d[arv] + 1
        else:
            d[arv] = 1
    return d
        
def grupeeri(c):
    sõnastik = {}
    Täishäälikud = ('a', 'e', 'i', 'o', 'u', 'ü','õ', 'ö', 'ä')
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Sümbolid'] = set()
    jär = list(c)
    for häälik in jär:
        häälik 
            if häälik.lower() in Täishäälikud:
                sõnastik['Täishäälikud'].add()
            