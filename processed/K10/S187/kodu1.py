def erinevad_sümbolid(blin):
    return(set(blin))

def sümbolite_sagedus(blin):
    hulk = set(blin)
    tulemus = {}
    for asi in hulk:
        tulemus[asi] = blin.count(asi)
    return(tulemus)

def grupeeri(blin):
    tais = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü']
    kaas = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y']
    tulemus = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    loetud = []
    for taht in blin:
        if taht not in loetud:
            if taht in tais:
                tulemus['Täishäälikud'].add((taht, blin.count(taht)))
            elif taht in kaas:
                tulemus['Kaashäälikud'].add((taht, blin.count(taht)))
            else:
                tulemus['Muud'].add((taht, blin.count(taht)))
            loetud.append(taht)
    return(tulemus)