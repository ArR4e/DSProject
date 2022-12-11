def erinevad_sümbolid(sõne):
    tähed = set(sõne)
    return tähed
    
d = {}
def sümbolite_sagedus(sõne):
    for el in sõne:
        if el in d:
            d[el] = d[el] + 1
        else:
            d[el] = 1
    return d


def grupeeri(sõne):
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    kaashäälikud = "bcdfghjkqQlmnprsšzžtvwxyBCDFGHJKLMNPRSŠZŽTVWXY"
    täis = {}
    kaas = {}
    muud = {}
    for täht in sõne:
        if täht in täishäälikud:
            if täht in täis:
                täis[täht] = täis[täht] + 1
            else:
                täis[täht] = 1
        elif täht in kaashäälikud:
            if täht in kaas:
                kaas[täht] = kaas[täht] + 1
            else:
                kaas[täht] = 1
        else:
            if täht in muud:
                muud[täht] = muud[täht] + 1
            else:
                muud[täht] = 1
    t = set(täis.items())
    k = set(kaas.items())
    m = set(muud.items())
    return {"Täishäälikud" : t, "Kaashäälikud" : k, "Muud" : m}