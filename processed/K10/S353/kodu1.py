def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    järjend = list(sõne)
    sõnastik = {}
    for täht in järjend:
        sõnastik[täht] = sõnastik.get(täht, 0) + 1
    return sõnastik
def grupeeri(sõne):
    täishäälikud = set('aeiouüõöä') | set('aeiouüõöä'.upper())
    kaashäälikud = set('qwrtypsdfghjklzxcvbnm') | set('qwrtypsdfghjklzxcvbnm'.upper())
    täishäälikuidsõnes=set()
    kaashäälikuidsõnes = set()
    muidsõnes = set()
    for täht in list(sõne):
        if täht in täishäälikud:
            palju = sõne.count(täht)
            täishäälikuidsõnes.add((täht, palju))
        elif täht in kaashäälikud:
            palju = sõne.count(täht)
            kaashäälikuidsõnes.add((täht, palju))
        else:
            palju = sõne.count(täht)
            muidsõnes.add((täht, palju))
    return {'Täishäälikud': täishäälikuidsõnes, 'Kaashäälikud': kaashäälikuidsõnes, 'Muud': muidsõnes}
grupeeri("sõida tasa üle silla")
        