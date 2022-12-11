def erinevad_sümbolid(sõne):
    erinevad=[]
    for el in sõne:
        if el not in erinevad:
            erinevad.append(el)
    return erinevad

def sümbolite_sagedus(sõne):
    järjend=[]
    sõnastik={}
    for el in sõne:
        x = el.strip().split(" ")
        järjend += x
    for i in järjend:
        sõnastik[i]=sõnastik.get(i, 0)+1
    return sõnastik

def grupeeri(sõne):
    täishäälikud=("a","e","i", "o","u","õ","ä","ü","ö")
    kaashäälikud=("k","p","t", "g","b","d","l","m","n", "r","v", "j","s","h")
    järjend=[]
    sõnastik={}
    s2={}
    s3={}
    s4={}
    hulk1=[]

    for el in sõne.lower():
        järjend += el.strip().split(" ")
    for i in järjend:
        if i in täishäälikud:
            s2[i]=s2.get(i, 0)+1
        elif i in kaashäälikud:
            s3[i]=s3.get(i, 0)+1
        else:
            s4[i]=s4.get(i, 0)+1
            
    sõnastik["Täishäälik"]=(s2)
    sõnastik["Kaashäälik"]=(s3)
    sõnastik["Muu"]=(s4)

    return sõnastik
    
    
