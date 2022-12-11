def erinevad_sümbolid(sone):
    s1 = set(sone)
    return (s1)
    
def sümbolite_sagedus(sone):
    freq={}
    for el in sone:
        for täht in el:
            if täht not in freq:
                freq[täht] = 0
            freq[täht] += 1
    return freq

def grupeeri(sone):
    taishaalikud = "aeuioüõäöAEUIOÜÕÄÖ"
    kaashaalikud = "qwrtypsdfghjklzxcvbnmQWERTYPSDFGHJKLZXCVBNM"
    sega = sümbolite_sagedus(sone)
    taishaalik = set()
    kaashaalik = set()
    muu = set()
    kokku = {}
    for i in sega:
        if i in taishaalikud:
            taishaalik.add((i,sega[i]))
        elif i in kaashaalikud:
            kaashaalik.add((i,sega[i]))
        else:
            muu.add((i, sega[i]))
    kokku["Täishäälikud"] = taishaalik
    kokku["Kaashäälikud"] = kaashaalik
    kokku["Muud"] = muu
    return kokku


print(erinevad_sümbolid("tere olen armand"))
print(sümbolite_sagedus("tere olen armand"))
print(grupeeri("tere olen armand"))
