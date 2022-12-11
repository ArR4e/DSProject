def erinevad_sümbolid(st):
    return set(st)

def sümbolite_sagedus(st):
    sõnastik = {}
    hulk = erinevad_sümbolid(st)
    for a in hulk:
        sõnastik[a] = st.count(a)
    return sõnastik

def grupeeri(st):
    tähed = {}
    täishäälikud = "aeiouõüäöAEIOUÕÄÖÜ"
    th = set()
    kh = set()
    muud = set()
    for a in sümbolite_sagedus(st):
        if a in täishäälikud:
            th.add((a,sümbolite_sagedus(st)[a]))
        elif a not in täishäälikud and a.isalpha():
            kh.add((a,sümbolite_sagedus(st)[a]))
        else:
            muud.add((a,sümbolite_sagedus(st)[a]))
    tähed["Täishäälikud"] = th
    tähed["Kaashäälikud"] = kh
    tähed["Muud"] = muud
    return tähed
    
print(grupeeri("sõida tasa üle silla"))