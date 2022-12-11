import string
def erinevad_sümbolid(sõne):
    return set(sõne)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    järjend = list(sõne)
    for x in järjend:
        täht = järjend.count(x)
        sõnastik[x] = täht
    return sõnastik
        
def grupeeri(sõne):
    sõnastik = {}
    sõnastik['Täishäälikud'] = set()
    sõnastik['Kaashäälikud'] = set()
    sõnastik['Muud'] = set()
    järjend = list(sõne)
    for x in järjend:
        if x.lower() in ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']:
            sõnastik['Täishäälikud'].add((x, järjend.count(x)))
        elif x in list(string.punctuation) or x == ' ':
            sõnastik['Muud'].add((x, järjend.count(x)))
        else:
            sõnastik['Kaashäälikud'].add((x, järjend.count(x)))
    return sõnastik