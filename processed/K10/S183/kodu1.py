def erinevad_sümbolid(sõne):
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for j in range(len(sõne)):
        sõnad = list(sõne)
        if sõne[j] in sõnastik:
            sõnastik[sõne[j]] += 1
        else:
            sõnastik[sõne[j]] = 1
    return sõnastik

def grupeeri(sõne):
    sõnastik = {}
    täis = "AEIOUÕÜÄÖaeiouõäöü"
    kaas = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrsšžtvwxyz"
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    tähed_ja_sümbolid= "ABCDEFGHIJKLMNOPQRSTUVWõäöüXYZabcdefghijklmnopqrsšzžtuvwõäöüxy ,()[]{}\€$£@.-;:?=/&%¤!?'"
    sagedus = sümbolite_sagedus(sõne)
    for i in tähed_ja_sümbolid:
        if i in täis:
            if i in sagedus:
                sõnastik["Täishäälikud"].add((i, sagedus[i]))
        elif i in kaas:
            if i in sagedus:
                sõnastik["Kaashäälikud"].add((i, sagedus[i]))
        else:
            if i in sagedus:
                sõnastik["Muud"].add((i, sagedus[i]))            
    return sõnastik
