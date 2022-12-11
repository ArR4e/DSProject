def erinevad_sümbolid(sõne):
    hulk = set()
    for el in sõne:
        if el not in hulk:
            hulk.add(el)
    return hulk
       
def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        if el not in sõnastik:
            sõnastik[el]=sõne.count(el)
    return sõnastik

def grupeeri(sõne):
    täis = ['a','A','e','E','i','I','o','O','u','U','õ','Õ','ä','Ä','ö','Ö','ü','Ü']
    kaas = ['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','š','Š','z','Z','ž','Ž','t','T','v','V','w','W','x','X','y','Y']
    sõnastik = {"Täishäälikud":"TERE"}
    täis_s = set()
    kaas_s = set()
    muu_s = set()
    for el in sõne:
        if el in täis:
            täis_s.add((el, sõne.count(el)))
        elif el in kaas:
            kaas_s.add((el, sõne.count(el)))
        else:
            muu_s.add((el, sõne.count(el)))
    sõnastik['Täishäälikud']=täis_s
    sõnastik['Kaashäälikud']=kaas_s
    sõnastik['Muud']=muu_s
    return sõnastik