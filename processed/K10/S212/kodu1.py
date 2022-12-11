def erinevad_sümbolid(sone):
    chars = set()
    for char in sone:
        chars.add(char)
    return chars

def sümbolite_sagedus(sone):
    chars = {}
    for el in sone:
        chars[el] = 0
    for char in sone:
        chars[char] += 1
    return chars

def grupeeri(sone):
    taishaalikud = ['a', 'e', 'i', 'o', 'u', 'ö', 'ä', 'õ', 'ü']
    kaashaalikud = ['b', 'c', 'd', 'f', 'g', 'h', 'z', 'ž', 's', 'š', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y', 'z']
    taisset = set()
    kaasset = set()
    muuset = set()
    sagedus = sümbolite_sagedus(sone)
    for char in sagedus:
        if char.lower() in taishaalikud:
            taisset.add((char,sagedus[char]))
        elif char.lower() in kaashaalikud:
            kaasset.add((char,sagedus[char]))
        else:
            muuset.add((char,sagedus[char]))
    chars = {'Täishäälikud':taisset,'Kaashäälikud':kaasset,'Muud':muuset}
    return chars


print(grupeeri("sõida tasa üle silla"))
