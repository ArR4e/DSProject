def erinevad_sümbolid(sõne):
    sümbolid= set(sõne)
    return sümbolid

def sümbolite_sagedus(sõne):
    sõ = set(sõne)
    s={}
    for i in sõ:
        s[i]=0
    sümbolid = list(sõne)
    for i in sümbolid:
        s[i]=s[i]+1
    return s
   
def grupeeri(sõne):
    g={}
    sõ=set(sõne)
    g["Täishäälikud"]= set()
    g["Kaashäälikud"]= set()
    g["Muud"]= set()
    s= sümbolite_sagedus(sõne)
    for el in sõ:
        if el.lower() in "vxycwqjlmnrshfšzžkptgbd":
            g["Kaashäälikud"].add((el,s[el]))
        elif el.lower() in "aeiouõäöü":
            g["Täishäälikud"].add((el,s[el]))
        else:
            g["Muud"].add((el,s[el]))
    return(g)