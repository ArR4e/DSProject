def erinevad_sümbolid(sõne):
    erinevad = set(sõne)
    return erinevad

# def sümbolite_sagedus(sõne):
#     d = {}
#     for sümbol in sõne:
#         if sümbol in d:
#             d[sümbol] = d[sümbol] + 1
#         else:
#             d[sümbol] = 1
#     return d

def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        d[sümbol] = d.get(sümbol,0) + 1
    return d


def grupeeri(sõne):
    sõnastik = {}
    sõnastik["Täishäälikud"] = set()
    sõnastik["Kaashäälikud"] = set()
    sõnastik["Muud"] = set()
    täishäälikud = {'a','e','i','o','u','õ','ä','ö','ü',
                    'A','E','I','O','U','Õ','Ä','Ö','Ü'}
    kaashäälikud = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','z','ž','w',
                    'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Y','Z','Ž','W'}
    
    for võti in sõne:
        if võti in täishäälikud:
            arv = sõne.count(võti)
            sõnastik["Täishäälikud"].add((võti,arv))
        elif võti in kaashäälikud:
            arv = sõne.count(võti)
            sõnastik["Kaashäälikud"].add((võti,arv))
        else:
            arv = sõne.count(võti)
            sõnastik["Muud"].add((võti,arv))
    
    return sõnastik
    


    
    
    