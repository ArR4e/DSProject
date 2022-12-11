#kodutöö 10.1
def erinevad_sümbolid(x):
    return set(x)

def sümbolite_sagedus(x):
    kordused = {}
    for i in x:
        kordused[i] = kordused.get(i, 0) + 1
    return kordused

def grupeeri(x):
    #teen hulgad, kus märgistan ära täis- ja kaashäälikud
    th = {"a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"}
    kh = {"h", "j", "l", "m", "n", "r", "s", "v", "k", "p", "t", "g", "b", "d"}
    #teen sõnastikud, kuhu hakkan lisama vastavaid häälikuid
    täishäälikud = {}
    kaashäälikud = {}
    muud = {}
    #kontrollin, kuhu iga täht kuulub ning lisan ta vastavasse sõnastikku
    for i in x:
        if i in th:
            täishäälikud[i] = täishäälikud.get(i, 0)+1
        elif i in kh:
            kaashäälikud[i] = kaashäälikud.get(i, 0)+1
        else:
            muud[i] = muud.get(i, 0)+1

    #teen uue sõnastiku, kuhu grupeerin nad kõik kokku 
    grupeering = {
                "Täishäälikud" : täishäälikud, 
                "Kaashäälikud" : kaashäälikud,
                "Muud" : muud}
    return grupeering
    