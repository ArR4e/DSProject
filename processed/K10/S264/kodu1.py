def erinevad_sümbolid(sõne):
    sümbolid = set(sõne)
    return sümbolid

def sümbolite_sagedus(sõne):
    d = {}
    for märk in sõne:
        d[märk] = d.get(märk, 0) + 1
    return d

täishäälikud = 'aeiouõäöüAEIOUÕÄÖÜ'
kaashäälikud = 'bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTVWXY'
def grupeeri(sõne):
    mitu = []
    s = {}
    s['Täishäälikud'] = set()
    s['Kaashäälikud'] = set()
    s['Muud'] = set()
    for märk in sõne:
        if märk in täishäälikud:
            mitu = sõne.count(märk)
            vokaale = list(märk) + list(str(mitu))
            vokaale[1] = int(vokaale[1])
            vokaale = tuple(vokaale)
            s['Täishäälikud'].add(vokaale)
        elif märk in kaashäälikud:
            mitu = sõne.count(märk)
            konsonante = list(märk) + list(str(mitu))
            konsonante[1] = int(konsonante[1])
            konsonante = tuple(konsonante)
            s['Kaashäälikud'].add(konsonante)
        else:
            mitu = sõne.count(märk)
            muid = list(märk) + list(str(mitu))
            muid[1] = int(muid[1])
            muid = tuple(muid)
            s['Muud'].add(muid)
    return s
    
print(grupeeri('Kui ma kirjutan niisama, siis on okei'))