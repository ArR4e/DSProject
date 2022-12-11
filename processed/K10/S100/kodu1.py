def erinevad_sümbolid(sone):
    arr = []
    for i in sone:
        if i not in arr:
            arr.append(i)
    return set(arr)


def sümbolite_sagedus(sone):
    dic = {}
    if len(sone) == 0:
        return dic
    keys = erinevad_sümbolid(sone)
    for i in keys:
        dic[i] = sone.count(i)
    return dic

def grupeeri(sone):
    tais = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kaas = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    sisend = sümbolite_sagedus(sone)
    taisarr = []
    kaasarr = []
    muudarr = []
    for i in sisend:
        if i.lower() in tais:
            taisarr.append((i, sisend[i]))
        elif i.lower() in kaas:
            kaasarr.append((i, sisend[i]))
        else:
            muudarr.append((i, sisend[i]))
    dic = {}
    dic["Täishäälikud"] = set(taisarr)
    dic["Kaashäälikud"] = set(kaasarr)
    dic["Muud"] = set(muudarr)
    return dic