def erinevad_sümbolid(sõne):
    
    hulk = set(sõne)
    return hulk

def sümbolite_sagedus(sõne1):
    
    sümbolid = list(sõne1)
    
    sõnastik = {}
    
    for el in sümbolid:
        arv = sümbolid.count(el)
        sõnastik[el] = arv
    return(sõnastik)
    
def grupeeri(sõne2):
    
    täishäälikud = {'a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü'}
    kaashäälikud = set("bcdfghjklmnpqrsšzžtvwxyBCDFGHJKLMNPQRSŠZŽTUVWXY")
    grupeering={}
    täis_hulk = set()
    kaas_hulk = set()
    muu_hulk = set()
    
    for el in erinevad_sümbolid(sõne2):
            
            
        if el in täishäälikud:
            
            sagedus_dict = sümbolite_sagedus(sõne2)
            korduvus = sagedus_dict[el]
            täis_hulk.add((el, korduvus))
            
        elif el in kaashäälikud:
            
            sagedus_dict = sümbolite_sagedus(sõne2)
            korduvus = sagedus_dict[el]
            kaas_hulk.add((el, korduvus))
        
        else:
            
            sagedus_dict = sümbolite_sagedus(sõne2)
            korduvus = sagedus_dict[el]
            muu_hulk.add((el, korduvus))

    grupeering["Täishäälikud"] = täis_hulk
    grupeering["Kaashäälikud"] = kaas_hulk
    grupeering["Muud"] = muu_hulk

    return(grupeering)