def erinevad_sümbolid(sõne): #f. erinevad_sümbolid
     hulk = set(sõne)
     for el in sõne:
         x = set(sõne)
         return x

def sümbolite_sagedus(sõne): #f. sümbolite_sagedus
    sõnastik = {i: sõne.count(i) for i in sõne}
    return sõnastik

def grupeeri(sõne): #f. grupeeri
    sõnastik = sümbolite_sagedus(sõne)
    häälik = {'a','e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü'}
    kaashäälik = {'q', 'Q', 'c', 'C', 'y', 'Y', 'w', 'W', 'j', 'x', 'X', 'l', 'm', 'n', 'r', 'v', 'k', 'p', 't', 'g', 'b', 'd', 'f', 'h', 's', 'š', 'z', 'ž', 'J', 'L', 'M', 'N', 'R', 'V', 'K', 'P', 'T', 'G', 'B', 'D', 'F', 'H', 'S', 'Š', 'Z', 'Ž'}
    ds = {}
    vowel = set()
    notvowel = set()
    muud = set()
    
    for tahe in sõne:
        if tahe in häälik:
            vowel.add((tahe, sõnastik[tahe]))
        elif tahe in kaashäälik:
            notvowel.add((tahe, sõnastik[tahe]))
        else:
            muud.add((tahe, sõnastik[tahe]))
            
    ds['Täishäälikud'] = vowel
    ds['Kaashäälikud'] = notvowel
    ds['Muud'] = muud
    return ds

sõne = 'erinevad_sümbolid'
sõnastik = grupeeri(sõne)
print(sõnastik)
