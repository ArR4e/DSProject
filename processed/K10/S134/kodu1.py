def erinevad_sümbolid(s):
    return(set(s))

def sümbolite_sagedus(s):
    sõnastik = {}
    for sümbol in s:
        if sümbol in sõnastik:
            sõnastik[sümbol] = sõnastik[sümbol] + 1
        else:
            sõnastik[sümbol] = 1
    return sõnastik

def grupeeri(s):
    sõnastik = {}
    sõnastik["täishäälik"] = set()
    sõnastik["kaashäälik"] = set()
    sõnastik["sümbol"] = set()
    sagedus = sümbolite_sagedus(s)
    s.split(" ")
    for võti in s:
        if võti.lower() in  "aeiouõäöü":
            sõnastik["täishäälik"].add(tuple(sümbolite_sagedus(s)))
        elif võti.lower() in "bdfghjklmnprsšzžtv":
            sõnastik["kaashäälik"].add(tuple(sümbolite_sagedus(s)))
        else:
            sõnastik["sümbol"].add(tuple(sümbolite_sagedus(s)))
        return sõnastik
grupeeri("sõida tasa üle silla")
            
        
    
    
         
     