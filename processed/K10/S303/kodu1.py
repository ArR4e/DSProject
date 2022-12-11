def erinevad_sümbolid(sõna):
    return set(sõna)

def sümbolite_sagedus(sõna):
    sõnastik = {}
    for sümbol in sõna:
        sõnastik[sümbol] = sõna.count(sümbol)
    return sõnastik

def grupeeri(sõna):
    täishäälikud = 'aeiouõüöäAEIOUÜÕÖÄ'
    kaashäälikud = 'bcdfghjklmnprsšzžtvwxyzqBCDFGHJKLMNPRSŠZŽTVWXYZQ'
    sõnastik = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    for sümbol in sõna:
        if sümbol in täishäälikud:
            sõnastik['Täishäälikud'].add((sümbol, sõna.count(sümbol)))
        elif sümbol in kaashäälikud:
            sõnastik['Kaashäälikud'].add((sümbol, sõna.count(sümbol)))
        else:
            sõnastik['Muud'].add((sümbol, sõna.count(sümbol)))
    return sõnastik
        