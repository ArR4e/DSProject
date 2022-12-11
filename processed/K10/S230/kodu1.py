def erinevad_sümbolid(a):
    hulk=set(a)
    return hulk

def sümbolite_sagedus(a):
    a=list(a)
    sõnastik={}
    for täht in a:
        sõnastik[täht]=sõnastik.get(täht,0)+1
    return sõnastik

def grupeeri(a):
    Täishäälikud=('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Õ', 'Ä', 'Ö', 'Ü')
    Kaashäälikud=('B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'Š', 'š', 'Z', 'z', 'Ž', 'ž', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y')
    sõnastik={}
    sõnastik["Täishäälikud"]=set()
    sõnastik["Kaashäälikud"]=set()
    sõnastik["Muud"]=set()
    s=sümbolite_sagedus(a)
    for täht in s:
        if täht in Täishäälikud:
            sõnastik["Täishäälikud"].add((täht,s[täht]))
        elif täht in Kaashäälikud:
            sõnastik["Kaashäälikud"].add((täht,s[täht]))
        else:
            sõnastik["Muud"].add((täht,s[täht])) 
    return sõnastik