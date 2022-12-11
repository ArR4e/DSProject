def erinevad_sümbolid(s):
    return set(s)

def sümbolite_sagedus(s):
    sümbolite_sagedus_dict = dict.fromkeys(s, 0)
    for i in s:
        sümbolite_sagedus_dict[i] += 1
    return sümbolite_sagedus_dict

def grupeeri(s):
    täishäälikud = 'aeiouõäöüAEIOUÕÄÖÜ'
    kaashäälikud = 'bdfghjklmnprsšzžtvxywqcBDFGHJKLMNPRSŠZŽTVXYWQC'
    sümbolite_sagedus_dict = sümbolite_sagedus(s)
    Täish = set()
    Kaash = set()
    Muud = set()
    grouped_dict = {'Täishäälikud': {},'Kaashäälikud': {},'Muud':{}}
    for key, value in sümbolite_sagedus_dict.items():
        if key in täishäälikud:
            Täish.add((key, value))
        elif key in kaashäälikud:
            Kaash.add((key, value))
        else:
            Muud.add((key, value))
            
    grouped_dict['Täishäälikud'] = Täish
    grouped_dict['Kaashäälikud'] = Kaash
    grouped_dict['Muud'] = Muud

    return grouped_dict
            
print(grupeeri("Minesi VARRo Voogla123%%/"))
