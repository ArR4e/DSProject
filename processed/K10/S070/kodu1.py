def erinevad_sümbolid(sõne):
    saadud_tähed = set(sõne)
    return saadud_tähed

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht] += 1
        else:
            sõnastik[täht] = 1
    return sõnastik

def grupeeri(sõne):
    täishäälikud = set("aeiouäõüö")
    kaashäälikud = set("qwrtypsdfghjklzxcvbnm")
    tähed = sümbolite_sagedus(sõne)
    vokaal = set()
    konsonant = set()
    muu = set()
    for täht, väärtus in tähed.items():
        if täht in täishäälikud:
            vokaal.add((täht, väärtus))
        if täht in kaashäälikud:
            konsonant.add((täht, väärtus))
        else:
            muu.add((täht, väärtus))
    sõnastik = {'Täishäälikud' : vokaal,
                'Kaashäälikud' : konsonant,
                'Muu' : muu}
    return sõnastik
            
            
    



a = erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
b = sümbolite_sagedus("Hei hopsti, väikevend!")
c = grupeeri("sõida tasa üle silla")
            
        