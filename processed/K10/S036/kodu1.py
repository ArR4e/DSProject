def erinevad_sümbolid(sõna):
    
    sisu = sõna.split()
    hulk = set()
    for i in range(len(sisu)):
        for j in sisu[i]:
            hulk.update(j)
    if " " in sõna:
        hulk.add(" ")
    return hulk
def sümbolite_sagedus(sõna):
    
    sõnastik = dict()
    for i in sõna:
        if i in sõnastik:
            sõnastik[i] = (sõnastik[i] + 1)
        else:
            sõnastik[i]= 1
    return sõnastik
def grupeeri(sõna):
    t_häälik = "aeiouõäöüAEIOUÕÄÖÜ"
    k_häälik = "bdghjklmnprstvxwqyczfBDGHJKLMNPRSTVXWQYCZF"
    vahe_sõnastik = sümbolite_sagedus(sõna)
    key_list = list(vahe_sõnastik.keys())
    sõnastik = dict()
    t_h = set()
    k_h = set()
    m = set()
   
    for i in key_list:
        if i in t_häälik:           
           t_h.update(tuple([(i,vahe_sõnastik[i])]))
        elif i in k_häälik: 
            k_h.update(tuple([(i,vahe_sõnastik[i])])) 
        else:
            m.update(tuple([(i,vahe_sõnastik[i])]))
    sõnastik["Täishäälikud"] = t_h
    sõnastik["Kaashäälikud"] = k_h
    sõnastik["Muud"]= m
    return sõnastik
print(grupeeri("sõida tasa üle silla"))
