def erinevad_sümbolid(a):
    hulk = set()
    for i in a:
        if i not in hulk:
            hulk.add(i)
    return hulk
def sümbolite_sagedus(a):
    sõnastik = dict()
    järj = []
    for i in a:
        järj.append(i)
    for täht in järj:
        if täht in sõnastik:
            sõnastik[täht] = sõnastik[täht] + 1
        else:
            sõnastik[täht] = 1
    return sõnastik
def grupeeri(a):
    sõnastik = dict()
    õigesõnastik = dict()
    thh = set()
    khh = set()
    muu = set()
    th = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    kh = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    järj = []
    for i in a:
        järj.append(i)
    for täht in järj:
        if täht in sõnastik:
            sõnastik[täht] = sõnastik[täht] + 1
        else:
            sõnastik[täht] = 1
    for i in sõnastik:
        if i[0].lower() in th:
            a = (i[0], sõnastik[i[0]])
            thh.add(a)
        elif i[0].lower() in kh:
            a = (i[0], sõnastik[i[0]])
            khh.add(a)
        else:
            a = (i[0], sõnastik[i[0]])
            muu.add(a)
    õigesõnastik["Täishäälikud"] = thh
    õigesõnastik["Kaashäälikud"] = khh
    õigesõnastik["Muud"] = muu
    return õigesõnastik