def erinevad_sümbolid(s):
    return set(s)

def sümbolite_sagedus(s):
    sõnastik={}
    for el in erinevad_sümbolid(s):
        sõnastik[el]=s.count(el)
    return sõnastik

def grupeeri(s):
    täishäälikud={'a','e','i','o','u','õ','ä','ö','ü'}
    kaashäälikud={'k','p','t','g','b','d','s','v','z','l','m','n','j','h','f','š','r','ž','q','w','x','y','c'}
    sõnastik2={}
    sõnastik2['Täishäälikud']=set()
    sõnastik2['Kaashäälikud']=set()
    sõnastik2['Muud']=set()
    for võti in sõnastik2:
        for el in erinevad_sümbolid(s):
            if el.lower() in täishäälikud:
                sõnastik2['Täishäälikud'].add((el,sümbolite_sagedus(s)[el]))
            elif el.lower() in kaashäälikud:
                sõnastik2['Kaashäälikud'].add((el,sümbolite_sagedus(s)[el]))
            else:
                sõnastik2['Muud'].add((el,sümbolite_sagedus(s)[el]))
    return sõnastik2
            
            


    