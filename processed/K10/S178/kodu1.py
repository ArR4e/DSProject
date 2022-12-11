def erinevad_sümbolid(sisend):
    return(set(sisend))


def sümbolite_sagedus(sisend):
    d = {}
    for täht in sisend:
        if täht in d:
            d[täht] = d[täht] + 1
        else:
            d[täht] = 1
    return(d)

def grupeeri(sisend):
    Täishäälikud = {'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ü', 'ö', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü'}
    Kaashäälikud = {'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'Z', 'V', 'Š', 'Ž'}
    d2_t = {}
    d2_k = {}
    Muud = {}
    for täht in sisend:
        if täht in Täishäälikud:
            if täht in d2_t:
                d2_t[täht] = d2_t[täht] + 1
            else:
                d2_t[täht] = 1
        elif täht in Kaashäälikud:
            if täht in d2_k:
                d2_k[täht] = d2_k[täht] + 1
            else:
                d2_k[täht] = 1
        else:
            if täht in Muud:
                Muud[täht] = Muud[täht] + 1
            else:
                Muud[täht] = 1
    Vastus = {
        'Täishäälikud' : d2_t,
        'Kaashäälikud' : d2_k,
        'Muud' : Muud
        }
    return(Vastus)

print(grupeeri('jüriöö ülestõus'))

