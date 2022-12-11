def erinevad_sümbolid(text):
    hulk = set()
    for s in text:
        if(s not in hulk):
            hulk.add(s)
        return hulk
    
def sümbolite_sagedus(text):
    sonastik = {}
    symbolid = erinevad_sümbolid(text)
    for s in symbolid:
        sonastik[s] = text.count(s)
    return sonastik
def grupeeri(text):
    sonastik = {}
    sonTais = {}
    sonKaas = {}
    sonMuud = {}
    taisHaalik = "AEIOUÕÄÖÜ"
    kaasHaalik = "HJLMNRSVKPTGBDKPTFŠZŽ"
    symbolidSagedus = sümbolite_sagedus(text)
    for s in symbolidSagedus:
        if s.upper() in taisHaalik:
            sonTais[s] = symbolidSagedus[s]
        elif s.upper() in kaasHaalik:
            sonKaas[s] = symbolidSagedus[s]
        else:
            sonMuud[s] = symbolidSagedus[s]
            
    sonastik["Täishäälikud"] = list(sonTais.items())
    sonastik["Kaashäälikud"] = list(sonMuud.items())
    sonastik["Muud"] = list(sonMuud.items())
    
    return sonastik

sisendTestimiseks = "sõida tasa üle silla"
result1 = erinevad_sümbolid(sisendTestimiseks)
print("erinevad_sümbolid: "+str(result1))

result2 = sümbolite_sagedus(sisendTestimiseks)
print("sümbolite_sagedus: "+ str(result2))
result3 =grupeeri(sisendTestimiseks)
print("grupeeri:"+ str(result3))