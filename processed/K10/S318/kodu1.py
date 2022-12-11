def erinevad_sümbolid(e_sõne):
    hulk = set(e_sõne)
    return hulk

def sümbolite_sagedus(s_sõne):
    sümbolite_kordus= {}
    sümb_list = list(s_sõne.strip())
    for sõna in sümb_list:
        if sõna in sümbolite_kordus:
            sümbolite_kordus[sõna] = sümbolite_kordus[sõna] + 1
        else:
            sümbolite_kordus[sõna] = 1
    return sümbolite_kordus

def grupeeri(g_sõne):
    täishäälikud = {'a','e','i','o','u','õ','ü','ä','ö',}
    kaashäälikud = {'b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'q','x','y','c','w'}
    sümb_sagedus = sümbolite_sagedus(g_sõne)
    täish = set(g_sõne) & set(täishäälikud)
    kaash = set(g_sõne) & set(kaashäälikud)
    täis=[]
    kaas=[]
    muud=[]
    tagastus={}
    for t in täish:
        tupl=(t,sümb_sagedus[t])
        täis.append(tupl)
    for k in kaash:
        tupl=(k,sümb_sagedus[k])
        kaas.append(tupl)
    for m in sümb_sagedus:
        if m.lower() in täishäälikud:
            tupl=(m,sümb_sagedus[m])
            täis.append(tupl)
        elif m.lower() in kaashäälikud:
            tupl=(m,sümb_sagedus[m])
            kaas.append(tupl)
        elif m not in täishäälikud and m not in kaashäälikud:
            tupl=(m,sümb_sagedus[m])
            muud.append(tupl)
    tagastus['Täishäälikud'] = set(täis)
    tagastus['Kaashäälikud'] = set(kaas)
    tagastus['Muud'] = set(muud)
    return tagastus